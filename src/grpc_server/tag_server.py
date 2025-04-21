import grpc
from concurrent import futures
from src.proto import tag_pb2, tag_pb2_grpc
from ..services.tag_service import get_tag_by_id_service

class gRPCTagService(tag_pb2_grpc.gRPCTagServiceServicer):
    def __init__(self, app):
        self.app = app

    def GetTagById(self, request, context):
        with self.app.app_context():
            tag = get_tag_by_id_service(request.tag_id)
            if tag:
                return tag_pb2.GetTagByIdResponse(
                    id=str(tag['id']),
                    name=tag['name']
                )
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Tag not found")
                return tag_pb2.GetTagByIdResponse()

def run_grpc_server(app):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tag_pb2_grpc.add_gRPCTagServiceServicer_to_server(gRPCTagService(app), server)
    server.add_insecure_port('0.0.0.0:50054')  # Порт для gRPC сервера
    print("Tag gRPC Server started on port 50054")
    server.start()
    server.wait_for_termination()