# Docker
## Build and deploy
To build and deploy the Docker Image, navigate to the `webapps` folder and run:

   ```
   docker build -t rpizziol/my-prime-checker-app .
   docker push rpizziol/my-prime-checker-app
   ```

## Superuser rights
To avoid having to use `sudo` for every `docker` command, add your user to the `docker` group.
1. Check if docker group exists:
   ``` 
   grep docker /etc/group
   ```
2. If not, create it:
   ``` 
   sudo groupadd docker
   ```
3. Add your user to the `docker` group:
   ```
   sudo usermod -aG docker $USER
   ```
4. Restart your system and test:
   ```
   docker run hello-world
   ```
