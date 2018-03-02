python -m grpc_tools.protoc \
	-I./protodefn \
	--python_out=. \
	--grpc_python_out=. \
	protodefn/helloworld.proto
