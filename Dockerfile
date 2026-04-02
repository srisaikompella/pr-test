FROM alpine

COPY ./myapp /



ENTRYPOINT ["/myapp"]
