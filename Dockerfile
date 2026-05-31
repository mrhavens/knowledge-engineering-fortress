# Stage 1: Build the Hugo site
FROM klakegg/hugo:ext-alpine as builder
WORKDIR /src
COPY . .
RUN hugo

# Stage 2: Serve the static files with Nginx
FROM nginx:alpine
# Copy the custom nginx config if we had one, otherwise default is fine for static HTML
# Remove default nginx static assets
RUN rm -rf /usr/share/nginx/html/*
# Copy the compiled Hugo output from the builder stage
COPY --from=builder /src/public /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
