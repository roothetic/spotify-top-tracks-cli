# spotify-top-tracks-cli
Display your top Spotify songs in a table in your terminal.

## Installing Dependencies

Make sure you are in the project directory, then run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

## Setting up Spotify Client ID, Client Secret, and Redirect URI

To access Spotify's API, you'll need to create a Spotify application and obtain a **Client ID**, **Client Secret**, and **Redirect URI**. Follow these steps:

1. **Log in to the Spotify Developer Dashboard**  
   Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account. If you don’t have an account, you’ll need to create one.

2. **Create a New Application**  
   - Click on **"Create an App"**.
   - Enter an **App Name** and **App Description** (these can be anything meaningful to you).
   - Check the box to agree to Spotify's terms and click **"Create"**.

3. **Obtain Client ID and Client Secret**  
   - After creating the app, you'll be directed to the app dashboard.
   - In the **App Overview** section, you’ll see your **Client ID**. Click **"Show Client Secret"** to reveal your **Client Secret**. These two values will be used to authenticate your app with Spotify’s API.

4. **Set up the Redirect URI**  
   - Scroll down to the **Redirect URIs** section and click **"Edit Settings"**.
   - Under **Redirect URIs**, add the URI you plan to use for authentication, such as `http://localhost:8888/callback`.
   - Click **"Add"** and then **"Save"**.

5. **Add Client ID, Client Secret, and Redirect URI to Your Project**  
   - Create a `.env` file in the project directory.
   - In the `.env` file, add the following lines, replacing the placeholders with your actual values:

     ```plaintext
     CLIENT_ID=your_client_id_here
     CLIENT_SECRET=your_client_secret_here
     REDIRECT_URI=your_callback_uri
     CACHE_PATH=path/to/your_cache_file
     ```

### About `cache_path`

The `cache_path` parameter in Spotify’s authentication setup specifies where the authentication token cache file is stored. This cache holds the Access Token and Refresh Token, allowing the app to reuse these tokens for authentication without requiring the user to log in each time.

If `cache_path` is not specified, a default `.cache` file will be created in the current directory. You can set `cache_path` to a custom location if you want more control over where the cache file is stored.

The setup is now complete, and these values are ready to be used to connect to the Spotify API.


# Setting Up an Alias for the Command

To make it easier to run your script, you can create an alias in your shell configuration file (e.g., `.bashrc` or `.zshrc`). This will allow you to use a simple command like `spotify` to run your script directly.

## Step-by-Step Guide

1. **Open your shell configuration file**  
   Open your shell configuration file in a text editor. The file is usually:
   - `.bashrc` for Bash users (most Linux distributions)
   - `.zshrc` for Zsh users (macOS and some Linux distributions)

2. **Add the alias**
   In the file, add the following line to create an alias named spotify (you can change spotify to any name you prefer):

   ```plaintext
     alias spotify='python /path/to/main.py'
     ```

3. **Save and close the file**
   After adding the alias, save and close the file. If you’re using nano, you can save and exit by pressing CTRL + X, then Y to confirm, and Enter to save.

4. **Reload the shell configuration**
   To apply the changes, reload your shell configuration by running:

   ```bash
   source ~/.bashrc
   ```

   If you added the alias in .zshrc, use source ~/.zshrc instead.

Now, you can use the alias spotify to run your Python script with different options.