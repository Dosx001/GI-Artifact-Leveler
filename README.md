# GI-Artifact-Leveler
GI-Artifact-Leveler is a Python script to automate leveling your artifacts in Genshin Impact.
The script will go through your artifacts and decide to scrap them for XP. If the artifact stats
are exceptional the artifact will be lock. Else it will be leave it alone for manual intervention.
# Demo
Does not represent the final quality of the product.

The algorithm for scraping and locking artifacts is still being work on.
<iframe width="560" height="315" src="https://www.youtube.com/embed/BNTzZlS-Ld8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# How to Run
First thing you need to run GI-Artifact-Leveler is to download and install Tesseract.

(32 bit) [tesseract-ocr-w32-setup-v5.0.0.20211201.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0.20211201.exe)

(64 bit) [tesseract-ocr-w64-setup-v5.0.0.20211201.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0.20211201.exe)

For more information checkout.

https://github.com/tesseract-ocr/tesseract#installing-tesseract

Next, make sure to update the path where Tesseract is located on your computer in
[ utils/img2text.py ]( https://github.com/Dosx001/GI-Artifact-Leveler/blob/main/utils/img2text.py#L15 )
on line 15.
```python
tes.pytesseract.tesseract_cmd = r'YOUR\LOCAL\PATH\TO\Tesseract-OCR\tesseract.exe'
```

For now GI-Artifact-Leveler cannot run with a single screen setup. You need to run the game on your
main screen and the Python script on another screen.

To run the script open PowerShell as Administrator and navigate to GI-Artifact-Leveler directory.

Also the game cannot be in fullscreen, it must be Windowed.

When inside the game, go to artifacts and pick an artifact you want to level up.
Then pull up the Enhanced menu.
![Imgur](https://i.imgur.com/WgCC3as.png)

Make sure the top option to "Base EXP" so GI-Artifact-Leveler look through your low level artifacts
first.
![Imgur](https://i.imgur.com/Tcufg0t.png)

If no additional [ arguments ](#optional-arguments) are added when running the script move your
cursor to the first column of the in-game menu. And place the cursor on the upper corner of the
artifact like the image below. If your not sure click the artifact and check your cursor is inside
the red box. Make to unclick the red box before running the script.

![Imgur](https://i.imgur.com/McsBqVm.png)

Finally, to avoid moving your cursor Alt-Tab to PowerShell and run the following the command.

```powershell
python.exe .\main.py
```

## Optional Arguments
If there already some artifacts your using to leveling the current artifact or you want the
script start on a different column like following image try these arguments.
![Imgur](https://i.imgur.com/IDltpNL.png)

```powershell
python.exe .\main.py --total=4 --column=8
```
or
```powershell
python.exe .\main.py -c=4 -t=8
```
