import requests
from flask import jsonify
from ..db import db
from ..models import Tag

import grpc
from src.proto import user_pb2, user_pb2_grpc, post_pb2, post_pb2_grpc

user_channel = grpc.insecure_channel('127.0.0.1:50053') # 127.0.0.1 / user-api
user_stub = user_pb2_grpc.gRPCUserServiceStub(user_channel)

post_channel = grpc.insecure_channel('127.0.0.1:50055') # 127.0.0.1 / post-api
post_stub = post_pb2_grpc.gRPCPostServiceStub(post_channel)

def get_user_by_email(email):
    try:
        response = user_stub.GetUserByEmail(user_pb2.GetUserByEmailRequest(email=email))
        return {
            'id': response.id,
            'email': response.email,
            'name': response.name,
            'surname': response.surname,
            'role': response.role
        }
    except grpc.RpcError as e:
        print(f"Error fetching user by email: {e}")
        return None

def delete_tag_in_all_posts(tag_id):
    try:
        print(tag_id)
        request = post_pb2.RemoveTagRequest(tag_id=str(tag_id))
        response = post_stub.RemoveTagFromPosts(request)
        return 'Теги успешно удалены'
    except grpc.RpcError as e:
        print(f"Error deleting tag in all posts: {e}")
        return {
            'error': 'Ошибка при удалении тега во всех постах через post-api'
        }

def create_tag_service(data, current_user_email):
    try:
        name = data.get('name')

        user_current = get_user_by_email(current_user_email)
        if user_current['role'] != 'admin':
            return jsonify({'error': 'У вас недостаточно прав'}), 403

        if not name:
            return jsonify({'error': 'Название тега обязательно'}), 400

        existing_tag = Tag.query.filter(Tag.name == name, Tag.deleted_at.is_(None)).first()
        if existing_tag:
            return jsonify({'error': 'Тег с таким названием уже существует'}), 400

        new_tag = Tag(name=name)
        db.session.add(new_tag)
        db.session.commit()

        print('Тег создан')

        return jsonify({
            'id': new_tag.id,
            'name': new_tag.name,
            'created_at': new_tag.created_at
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


def delete_tag_service(tag_id, current_user_email):
    try:
        tag = Tag.query.filter(Tag.id == tag_id, Tag.deleted_at.is_(None)).first()

        user_current = get_user_by_email(current_user_email)
        if user_current.get('role') != 'admin':
            return jsonify({'error': 'У вас недостаточно прав'}), 403

        if not tag:
            return jsonify({'error': 'Тег не найден'}), 404

        db.session.delete(tag)
        db.session.commit()
        delete_tag_in_all_posts(tag.id)

        return jsonify({'message': 'Тег удален успешно'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500



def get_all_tags_service():
    try:
        tags = Tag.query.filter(Tag.deleted_at.is_(None)).all()
        tags_list = [{
            'id': tag.id,
            'name': tag.name,
        } for tag in tags]

        return jsonify(tags_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_tag_by_id_service(id):
    tag = Tag.query.filter_by(id=id).first()
    if tag:
        tag_data = {
            'id': tag.id,
            'name': tag.name
        }
        return tag_data
    return jsonify({'message': 'Тег не найден'}), 404
