# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from demo.proto import test_pb2 as demo_dot_proto_dot_test__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.simpleHello = channel.unary_unary(
        '/Greeter/simpleHello',
        request_serializer=demo_dot_proto_dot_test__pb2.HelloRequest.SerializeToString,
        response_deserializer=demo_dot_proto_dot_test__pb2.HelloReply.FromString,
        )
    self.serverStreamHello = channel.unary_stream(
        '/Greeter/serverStreamHello',
        request_serializer=demo_dot_proto_dot_test__pb2.HelloRequest.SerializeToString,
        response_deserializer=demo_dot_proto_dot_test__pb2.HelloReply.FromString,
        )
    self.clientStreamHello = channel.stream_unary(
        '/Greeter/clientStreamHello',
        request_serializer=demo_dot_proto_dot_test__pb2.HelloRequest.SerializeToString,
        response_deserializer=demo_dot_proto_dot_test__pb2.HelloReply.FromString,
        )
    self.biStreamHello = channel.stream_stream(
        '/Greeter/biStreamHello',
        request_serializer=demo_dot_proto_dot_test__pb2.HelloRequest.SerializeToString,
        response_deserializer=demo_dot_proto_dot_test__pb2.HelloReply.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def simpleHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def serverStreamHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def clientStreamHello(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def biStreamHello(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'simpleHello': grpc.unary_unary_rpc_method_handler(
          servicer.simpleHello,
          request_deserializer=demo_dot_proto_dot_test__pb2.HelloRequest.FromString,
          response_serializer=demo_dot_proto_dot_test__pb2.HelloReply.SerializeToString,
      ),
      'serverStreamHello': grpc.unary_stream_rpc_method_handler(
          servicer.serverStreamHello,
          request_deserializer=demo_dot_proto_dot_test__pb2.HelloRequest.FromString,
          response_serializer=demo_dot_proto_dot_test__pb2.HelloReply.SerializeToString,
      ),
      'clientStreamHello': grpc.stream_unary_rpc_method_handler(
          servicer.clientStreamHello,
          request_deserializer=demo_dot_proto_dot_test__pb2.HelloRequest.FromString,
          response_serializer=demo_dot_proto_dot_test__pb2.HelloReply.SerializeToString,
      ),
      'biStreamHello': grpc.stream_stream_rpc_method_handler(
          servicer.biStreamHello,
          request_deserializer=demo_dot_proto_dot_test__pb2.HelloRequest.FromString,
          response_serializer=demo_dot_proto_dot_test__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
