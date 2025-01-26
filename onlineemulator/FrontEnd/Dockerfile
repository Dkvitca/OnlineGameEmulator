# Build Stage
FROM node:current-alpine3.20 AS build

WORKDIR /app/

# Copy the necessary files for the build context
COPY ./package.json ./index.html ./register.html ./register.js ./script.js ./style.css  ./

# Install dependencies
RUN npm install

# Runtime Stage (Nginx)
FROM nginx:1.27.3-alpine

WORKDIR /usr/share/nginx/html

# Copy the built files from the build stage
COPY --from=build /app/index.html ./index.html
COPY --from=build /app/register.html ./register.html
COPY --from=build /app/register.js ./register.js
COPY --from=build /app/script.js ./script.js
COPY --from=build /app/style.css ./style.css
COPY ./data/ ./data/

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for web access
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
