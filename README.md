# SrtEditor
GUI to create SRT files.
# Prerequisites 
* Media player that allows .srt files (Example: [VLC](https://www.videolan.org/vlc/download-windows.html))
* [Basic K-Lite Codec Pack](https://codecguide.com/download_kl.htm)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
# Setup
### Windows
1. Add Miniconda to Path in System Variables to be able to use conda commands in Terminal of choice.
   - Go to System Properties -> Advanced Tab -> Environment Variables
   - Under System Variables, Select **Path** and **Edit**
   - Add Miniconda home folder and Scripts folder. 
     - C:\Users\\**youruser**\miniconda3
     - C:\Users\\**youruser**\miniconda3\Scripts
    - Select **Ok** and **Apply** where necessary.
2. Create environment ( See: [Creating environment from existing yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) )
   - Open preferred terminal and run `conda env create -f pathtoymlfile`
     - Replace `pathtoymlfile` with directory to yml file in repository (Example: C:\SrtEditor\srt_env.yml)
3. Test environment by using `conda activate srt` or just `activate srt` if first command does not work.
4. Deactive the environment by using `conda deactivate`.
5. Open project in Pycharm.
6. Add Python Interpreter
   - Open **Settings** by pressing **Ctrl + Alt + S** simultaneously or by selecting **Settings** under **File**.
   - Select **Python Interpreter** under  **Project**.
   - Select the "Gear" icon and then **Add** to create a new Python interpreter.
   - Select **Conda Environment** and then **Existing environment**.
   - The recently created srt environment and conda executable should be selected.
     - If not already selected, add the environment python.exe directory as interpreter path 
       (C:\Users\\**youruser**\miniconda2\env\srt\python.exe) 
     - If not already selected, add the conda executable directory as well
       (C:\Users\\**youruser**\miniconda3\Scripts\conda.exe) 
   - Press **Apply** and **Ok** to save changes. 
7. Add Configuration
   - Add new Python Configuration and name it accordingly
   - Select the main.py directory as **Script Path**
     (C:\SrtEditor\src\main\python\main.py)
   - Select recently created interpreter as the project's Python Interpreter.
   - Select **Apply** and **Ok** to save changes.
8. Run project.


# Basic Usage
1. Open video by clicking "Abrir Video"
2. Begin adding lyrics

![image](https://user-images.githubusercontent.com/30638262/113526022-d1e79d80-957d-11eb-835c-8b7bb6692d2e.png)

3. Use the time skip buttons at the top control media playback

![image](https://user-images.githubusercontent.com/30638262/113526115-533f3000-957e-11eb-9a48-b7c9b8c9d310.png)

4. Choose desired language. If both English and Spanish are chosen... English subtitles will be displayed above Spanish subtitles.

![image](https://user-images.githubusercontent.com/30638262/113526309-36efc300-957f-11eb-8a60-265be1169af0.png)

5. If there will be subtitles in Spanish, choose a desired emoji encapsulation from the drop down list under translation options. Currently these emojis are only inetgrated for Spanish translations.

![image](https://user-images.githubusercontent.com/30638262/113526378-73232380-957f-11eb-952c-93349f214f41.png)

6. When your subtitles are done click on "Crear SRT" to create your subtitles. This will then open the file location of where your file was saved.
7. To view your subtitles simply open your video in VLC. As long as your subtitle (.srt) files are in the same folder path as your video, VLC will auto detect your subtitles.
