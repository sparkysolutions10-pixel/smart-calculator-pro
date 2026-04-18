!pip install buildozer

# Upload your calculator.py folder as zip to Colab
# Extract it
!unzip calculator.py.zip -d calculator.py

# Change to directory
%cd calculator.py

# Build the APK
!buildozer android debug

# Download the APK
from google.colab import files
files.download('bin/smartcalculatorpro-0.1-debug.apk')