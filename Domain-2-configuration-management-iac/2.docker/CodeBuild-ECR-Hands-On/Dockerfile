FROM manifoldailearning/golang:1.12-alpine AS build
#Install git
RUN apk add --no-cache git
#Get the hello world package from a GitHub repository
RUN go get https://github.com/manifoldailearning/AWS-Certified-DevOps-Engineer-Professional/Domain-2-configuration-management-iac/2.docker/hello
WORKDIR /go/src/github.com/manifoldailearning/AWS-Certified-DevOps-Engineer-Professional/Domain-2-configuration-management-iac/2.docker/hello
# Build the project and send the output to /bin/HelloWorld 
RUN go build -o /bin/HelloWorld

FROM manifoldailearning/golang:1.12-alpine
#Copy the build's output binary from the previous build container
COPY --from=build /bin/HelloWorld /bin/HelloWorld
ENTRYPOINT ["/bin/HelloWorld"]