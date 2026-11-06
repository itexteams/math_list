import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang7_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            # Lựa chọn các bộ số (a, h, l) thỏa mãn tam giác vuông SO B: a^2 + h^2 = l^2
            params = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10), (5, 12, 13)]
            a_val, h_val, l_val = random.choice(params)

            a = Rational(a_val)
            h = Rational(h_val)
            l = Rational(l_val)

            CD_val = a * sqrt(2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Chi đoàn X dự định dựng một lều trại dã ngoại hình chóp tứ giác đều $S.ABCD$ có cạnh $SB = %s$, $CD = %s$. Chọn hệ trục tọa độ $Oxyz$ như hình vẽ.
                             \\begin{center}
                             	\\tikzset {_q88f22nqn/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_fv5xpqg6k}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
                             		rgb(37.5bp)=(0.97,0.91,0.11);
                             		rgb(49.96317182268415bp)=(0.4,0.21,0.04);
                             		rgb(100bp)=(0.4,0.21,0.04)}
                             	\\tikzset {_of6o856fq/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_xzmbbsa29}{150bp}{rgb(0bp)=(0.4,0.21,0.04);
                             		rgb(37.5bp)=(0.4,0.21,0.04);
                             		rgb(62.5bp)=(0.97,0.91,0.11);
                             		rgb(100bp)=(0.97,0.91,0.11)}
                             	\\tikzset {_jz05d07ch/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-135 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_6ujhux51a}{150bp}{rgb(0bp)=(0,0,0);
                             		rgb(37.5bp)=(0,0,0);
                             		rgb(49.76674216134208bp)=(0,0.5,0);
                             		rgb(50.26450565883091bp)=(0,0,0);
                             		rgb(50.51785605294364bp)=(0.49,0.83,0.13);
                             		rgb(100bp)=(0.49,0.83,0.13)}
                             	\\tikzset {_552ehhbt4/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-44 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_630ae09ir}{150bp}{rgb(0bp)=(0,0,0);
                             		rgb(37.5bp)=(0,0,0);
                             		rgb(48.15959930419922bp)=(0,0.5,0);
                             		rgb(49.35714176722935bp)=(0.49,0.83,0.13);
                             		rgb(50.479910714285715bp)=(0,0,0);
                             		rgb(100bp)=(0,0,0)}
                             	\\tikzset {_58otquets/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-141 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_511nhc61r}{150bp}{rgb(0bp)=(0,0,0);
                             		rgb(37.5bp)=(0,0,0);
                             		rgb(49.58817073277065bp)=(0,0.5,0);
                             		rgb(50bp)=(0.49,0.83,0.13);
                             		rgb(51.23214176722935bp)=(0,0,0);
                             		rgb(100bp)=(0,0,0)}
                             	\\tikzset {_5efc1f62u/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-21 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_b0xs9dkuy}{150bp}{rgb(0bp)=(0.72,0.67,0.04);
                             		rgb(45.05245753696987bp)=(0.72,0.67,0.04);
                             		rgb(47.66071319580078bp)=(0.97,0.91,0.11);
                             		rgb(51.67857033865793bp)=(0.69,0.64,0.03);
                             		rgb(100bp)=(0.69,0.64,0.03)}
                             	\\tikzset {_n6gkpi023/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformscale{1 }  }}}
                             	\\pgfdeclareradialshading{_17myf7ari}{\\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.97,0.91,0.11);
                             		rgb(18.91071319580078bp)=(0.97,0.91,0.11);
                             		rgb(25bp)=(0.58,0.53,0.04);
                             		rgb(400bp)=(0.58,0.53,0.04)}
                             	\\tikzset {_rsdjvn3qo/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                             	\\pgfdeclarehorizontalshading{_2m5z5mrzu}{150bp}{rgb(0bp)=(0.62,0.58,0.03);
                             		rgb(37.5bp)=(0.62,0.58,0.03);
                             		rgb(50bp)=(0.97,0.91,0.11);
                             		rgb(62.5bp)=(0.49,0.45,0.04);
                             		rgb(100bp)=(0.49,0.45,0.04)}
                             	\\tikzset{every picture/.style={line width=0.75pt}} 
                                 \\scalebox{0.7}{ 
                             	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.42 ] (362.33,191.87) .. controls (380.37,183.19) and (548.47,171.78) .. (577.79,182.64) .. controls (600.66,190.47) and (613.42,193.5) .. (589.06,200.01) .. controls (579.18,207.96) and (556.18,216.94) .. (521.86,221.73) .. controls (511.48,227.38) and (500.11,227.34) .. (461.87,223.47) .. controls (449.43,222.21) and (440.99,215.8) .. (428.49,214.35) .. controls (416.06,212.9) and (403.16,212.95) .. (399.62,207.83) .. controls (377.07,191.76) and (344.28,200.56) .. (362.33,191.87) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.42 ] (353.89,194.63) .. controls (373.89,184.63) and (560.23,171.5) .. (592.73,184) .. controls (618.09,193.01) and (632.23,196.5) .. (605.23,204) .. controls (594.28,213.14) and (568.78,223.48) .. (530.73,229) .. controls (519.23,235.5) and (506.62,235.46) .. (464.23,231) .. controls (450.44,229.55) and (441.09,222.17) .. (427.23,220.5) .. controls (413.46,218.84) and (399.16,218.89) .. (395.23,213) .. controls (370.23,194.5) and (333.89,204.63) .. (353.89,194.63) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ][fill={rgb, 255:red, 184; green, 141; blue, 23 }  ,fill opacity=1 ] (579.07,199.5) -- (497.03,222.4) -- (361.33,194.4) -- (453.33,179.4) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 155; green, 78; blue, 9 }  ,fill opacity=1 ] (490.33,202.4) -- (463.83,213.4) -- (397.26,201.33) -- (437.83,189.4) -- cycle ;
                             		\\path  [shading=_fv5xpqg6k,_q88f22nqn] (453.33,179.4) -- (564.85,200.22) -- (521.33,143.4) -- (465.33,117.9) -- cycle ; 
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ] (453.33,179.4) -- (564.85,200.22) -- (521.33,143.4) -- (465.33,117.9) -- cycle ;  
                             		\\path  [shading=_xzmbbsa29,_of6o856fq] (453.33,179.4) -- (361.33,194.4) -- (417.33,134.9) -- (465.33,117.9) -- cycle ; 
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ] (453.33,179.4) -- (361.33,194.4) -- (417.33,134.9) -- (465.33,117.9) -- cycle ; 
                             		\\draw [color={rgb, 255:red, 166; green, 154; blue, 11 }  ,draw opacity=1 ][line width=2.25]    (357.44,191.95) -- (351.27,200.5) ;
                             		\\draw [color={rgb, 255:red, 166; green, 154; blue, 11 }  ,draw opacity=1 ][line width=2.25]    (498.29,224.37) -- (500.27,234.83) ;
                             		\\draw [color={rgb, 255:red, 166; green, 154; blue, 11 }  ,draw opacity=1 ][line width=2.25]    (579.07,199.5) -- (587.27,210.17) ;
                             		\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (583.03,201.9) -- (497.03,222.4) -- (472.53,60.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (357.44,193.95) -- (358.23,190.3) -- (498.08,220.71) -- (497.29,224.37) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (498.89,223.74) -- (498.08,220.71) -- (576.23,199.88) -- (577.03,202.9) -- cycle ;
                             		\\path  [shading=_6ujhux51a,_jz05d07ch] (472.35,60.54) -- (476.04,57.81) -- (583.85,203.4) -- (580.16,206.13) -- cycle ; 
                             		\\draw   (472.35,60.54) -- (476.04,57.81) -- (583.85,203.4) -- (580.16,206.13) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 211; green, 233; blue, 134 }  ,fill opacity=1 ] (450.03,113.9) .. controls (457.02,110.4) and (468.54,105.69) .. (479.7,101.88) .. controls (487.03,133.4) and (495.03,207.9) .. (497.03,222.4) .. controls (485.03,215.9) and (486.03,224.4) .. (473.53,219.9) .. controls (465.53,221.4) and (477.03,195.4) .. (479.53,161.4) .. controls (469.03,163.9) and (444.53,141.9) .. (450.03,113.9) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 204; green, 233; blue, 134 }  ,fill opacity=1 ] (454.94,108.95) .. controls (449.68,102.61) and (445.09,109.97) .. (435.94,101.45) .. controls (415.42,126.62) and (363.05,181.25) .. (354.94,193.45) .. controls (369.29,193.03) and (371.45,195.84) .. (385.44,197.45) .. controls (392.52,202.45) and (394.85,182.84) .. (406.94,150.95) .. controls (417.94,161.45) and (448.31,136.78) .. (454.94,108.95) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (471.24,57.64) .. controls (477.74,87.14) and (477.74,81.14) .. (479.24,105.64) .. controls (467.24,111.14) and (449.24,113.64) .. (432.74,106.14) .. controls (453.24,80.14) and (453.74,81.14) .. (471.24,57.64) -- cycle ;
                             		\\path  [shading=_630ae09ir,_552ehhbt4] (469.57,57.89) -- (472.53,60.4) -- (356.86,197.14) -- (353.89,194.63) -- cycle ; 
                             		\\draw   (469.57,57.89) -- (472.53,60.4) -- (356.86,197.14) -- (353.89,194.63) -- cycle ;
                             		\\path  [shading=_511nhc61r,_58otquets] (471.24,57.64) -- (474.85,57.09) -- (500.67,228.43) -- (497.06,228.97) -- cycle ; 
                             		\\draw   (471.24,57.64) -- (474.85,57.09) -- (500.67,228.43) -- (497.06,228.97) -- cycle ; 
                             		\\path  [shading=_b0xs9dkuy,_5efc1f62u] (472.87,50.39) -- (481.53,64.17) -- (464.2,64.17) -- cycle ; 
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (472.87,50.39) -- (481.53,64.17) -- (464.2,64.17) -- cycle ; 
                             		\\path  [shading=_17myf7ari,_n6gkpi023] (469.09,46.74) .. controls (469.09,44.63) and (470.8,42.93) .. (472.9,42.93) .. controls (475.01,42.93) and (476.71,44.63) .. (476.71,46.74) .. controls (476.71,48.84) and (475.01,50.55) .. (472.9,50.55) .. controls (470.8,50.55) and (469.09,48.84) .. (469.09,46.74)(467.08,46.74) .. controls (467.08,43.52) and (469.69,40.91) .. (472.9,40.91) .. controls (476.12,40.91) and (478.72,43.52) .. (478.72,46.74) .. controls (478.72,49.95) and (476.12,52.56) .. (472.9,52.56) .. controls (469.69,52.56) and (467.08,49.95) .. (467.08,46.74) ; 
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ] (469.09,46.74) .. controls (469.09,44.63) and (470.8,42.93) .. (472.9,42.93) .. controls (475.01,42.93) and (476.71,44.63) .. (476.71,46.74) .. controls (476.71,48.84) and (475.01,50.55) .. (472.9,50.55) .. controls (470.8,50.55) and (469.09,48.84) .. (469.09,46.74)(467.08,46.74) .. controls (467.08,43.52) and (469.69,40.91) .. (472.9,40.91) .. controls (476.12,40.91) and (478.72,43.52) .. (478.72,46.74) .. controls (478.72,49.95) and (476.12,52.56) .. (472.9,52.56) .. controls (469.69,52.56) and (467.08,49.95) .. (467.08,46.74) ; 
                             		\\path  [shading=_2m5z5mrzu,_rsdjvn3qo] (470.05,55.13) -- (470.13,52.48) .. controls (470.17,51.02) and (471.44,49.87) .. (472.98,49.91) .. controls (474.51,49.95) and (475.72,51.17) .. (475.68,52.64) -- (475.6,55.29) -- cycle ; 
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ] (470.05,55.13) -- (470.13,52.48) .. controls (470.17,51.02) and (471.44,49.87) .. (472.98,49.91) .. controls (474.51,49.95) and (475.72,51.17) .. (475.68,52.64) -- (475.6,55.29) -- cycle ; 
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (469.94,63.95) -- (466.83,86.9) -- (459.33,99.4) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (472.33,65.4) -- (475.83,93.9) -- (470.83,83.9) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (469.94,63.95) -- (456.33,85.4) -- (444.33,95.9) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (477.8,69.57) -- (485.47,107.23) -- (489.13,149.9) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (454.56,101.77) .. controls (455.12,99.93) and (456.86,98.84) .. (458.44,99.32) .. controls (460.02,99.8) and (460.84,101.69) .. (460.28,103.52) .. controls (459.72,105.36) and (457.98,106.46) .. (456.4,105.98) .. controls (454.82,105.49) and (454,103.61) .. (454.56,101.77) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (455.47,102.05) .. controls (455.85,100.8) and (457.04,100.05) .. (458.11,100.38) .. controls (459.19,100.71) and (459.75,101.99) .. (459.37,103.25) .. controls (458.99,104.5) and (457.8,105.25) .. (456.72,104.92) .. controls (455.65,104.59) and (455.08,103.3) .. (455.47,102.05) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (466.22,99.44) .. controls (466.79,97.6) and (468.52,96.5) .. (470.1,96.99) .. controls (471.68,97.47) and (472.51,99.35) .. (471.95,101.19) .. controls (471.38,103.03) and (469.65,104.13) .. (468.07,103.64) .. controls (466.49,103.16) and (465.66,101.28) .. (466.22,99.44) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (467.13,99.72) .. controls (467.52,98.46) and (468.7,97.71) .. (469.78,98.04) .. controls (470.86,98.37) and (471.42,99.66) .. (471.04,100.91) .. controls (470.65,102.17) and (469.47,102.92) .. (468.39,102.59) .. controls (467.31,102.26) and (466.75,100.97) .. (467.13,99.72) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (443.89,100.11) .. controls (444.45,98.27) and (446.19,97.17) .. (447.77,97.65) .. controls (449.35,98.14) and (450.18,100.02) .. (449.61,101.86) .. controls (449.05,103.69) and (447.31,104.79) .. (445.73,104.31) .. controls (444.15,103.83) and (443.33,101.94) .. (443.89,100.11) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (444.8,100.38) .. controls (445.18,99.13) and (446.37,98.38) .. (447.45,98.71) .. controls (448.52,99.04) and (449.09,100.32) .. (448.7,101.58) .. controls (448.32,102.83) and (447.13,103.58) .. (446.06,103.25) .. controls (444.98,102.92) and (444.42,101.64) .. (444.8,100.38) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (462.22,76.77) .. controls (462.79,74.93) and (464.52,73.84) .. (466.1,74.32) .. controls (467.68,74.8) and (468.51,76.69) .. (467.95,78.52) .. controls (467.38,80.36) and (465.65,81.46) .. (464.07,80.98) .. controls (462.49,80.49) and (461.66,78.61) .. (462.22,76.77) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (463.13,77.05) .. controls (463.52,75.8) and (464.7,75.05) .. (465.78,75.38) .. controls (466.86,75.71) and (467.42,76.99) .. (467.04,78.25) .. controls (466.65,79.5) and (465.47,80.25) .. (464.39,79.92) .. controls (463.31,79.59) and (462.75,78.3) .. (463.13,77.05) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (452.89,90.11) .. controls (453.45,88.27) and (455.19,87.17) .. (456.77,87.65) .. controls (458.35,88.14) and (459.18,90.02) .. (458.61,91.86) .. controls (458.05,93.69) and (456.31,94.79) .. (454.73,94.31) .. controls (453.15,93.83) and (452.33,91.94) .. (452.89,90.11) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (453.8,90.38) .. controls (454.18,89.13) and (455.37,88.38) .. (456.45,88.71) .. controls (457.52,89.04) and (458.09,90.32) .. (457.7,91.58) .. controls (457.32,92.83) and (456.13,93.58) .. (455.06,93.25) .. controls (453.98,92.92) and (453.42,91.64) .. (453.8,90.38) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 193; green, 179; blue, 18 }  ,fill opacity=1 ] (463.89,89.77) .. controls (464.45,87.93) and (466.19,86.84) .. (467.77,87.32) .. controls (469.35,87.8) and (470.18,89.69) .. (469.61,91.52) .. controls (469.05,93.36) and (467.31,94.46) .. (465.73,93.98) .. controls (464.15,93.49) and (463.33,91.61) .. (463.89,89.77) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (464.8,90.05) .. controls (465.18,88.8) and (466.37,88.05) .. (467.45,88.38) .. controls (468.52,88.71) and (469.09,89.99) .. (468.7,91.25) .. controls (468.32,92.5) and (467.13,93.25) .. (466.06,92.92) .. controls (464.98,92.59) and (464.42,91.3) .. (464.8,90.05) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 193; green, 181; blue, 34 }  ,fill opacity=1 ] (481.37,63.36) .. controls (480.74,64.52) and (477.29,65.4) .. (473.13,65.4) .. controls (468.53,65.4) and (464.8,64.32) .. (464.8,62.98) .. controls (464.8,62.96) and (464.8,62.94) .. (464.8,62.92) -- (473.13,62.98) -- cycle ; \\draw   (481.37,63.36) .. controls (480.74,64.52) and (477.29,65.4) .. (473.13,65.4) .. controls (468.53,65.4) and (464.8,64.32) .. (464.8,62.98) .. controls (464.8,62.96) and (464.8,62.94) .. (464.8,62.92) ;  
                             		\\draw  [draw opacity=0] (479.21,61.85) .. controls (477.69,62.43) and (475.27,62.82) .. (472.53,62.82) .. controls (469.84,62.82) and (467.45,62.45) .. (465.92,61.87) -- (472.53,60.4) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ] (479.21,61.85) .. controls (477.69,62.43) and (475.27,62.82) .. (472.53,62.82) .. controls (469.84,62.82) and (467.45,62.45) .. (465.92,61.87) ;  
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (477.8,67.57) -- (493.8,105.9) -- (487.13,97.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (477.8,67.57) -- (520.47,153.9) -- (507.13,117.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (479.8,71.23) -- (533.8,142.9) -- (514.47,121.9) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (489.8,157.9) -- (498.13,189.57) -- (499.8,220.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (501.8,177.9) -- (504.47,199.9) -- (499.8,220.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (508.47,212.23) -- (528.47,207.57) -- (499.8,220.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (514.47,185.23) -- (505.8,213.9) -- (499.8,220.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (547.13,161.9) -- (576.23,199.88) -- (561.8,186.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (552.8,181.9) -- (576.23,199.88) -- (559.13,191.57) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (560.47,201.57) -- (576.23,199.88) -- (540.47,208.57) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (556.47,195.57) -- (576.23,199.88) -- (553.47,200.57) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (536.13,157.57) -- (558.13,182.57) -- (521.13,131.23) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (485.13,100.57) -- (499.13,178.23) -- (493.13,158.57) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (494.47,129.9) -- (503.8,149.9) -- (503.47,172.57) -- cycle ;
                             		\\draw  [dash pattern={on 0.84pt off 2.51pt}]  (435.47,104.83) .. controls (444,105.83) and (456.47,112.5) .. (477.47,103.83) ;
                             		\\draw  [dash pattern={on 0.84pt off 2.51pt}]  (574.13,199.17) -- (501.47,218.83) ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ][fill={rgb, 255:red, 143; green, 133; blue, 13 }  ,fill opacity=1 ] (591.95,206.85) -- (589.63,213.07) .. controls (589.5,213.42) and (588.44,213.35) .. (587.27,212.92) .. controls (586.1,212.48) and (585.25,211.84) .. (585.38,211.49) -- (587.7,205.26) .. controls (587.83,204.91) and (588.89,204.98) .. (590.06,205.42) .. controls (591.24,205.85) and (592.08,206.49) .. (591.95,206.85) .. controls (591.82,207.2) and (590.76,207.13) .. (589.59,206.69) .. controls (588.41,206.26) and (587.57,205.62) .. (587.7,205.26) ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ][fill={rgb, 255:red, 143; green, 133; blue, 13 }  ,fill opacity=1 ] (504.41,231.08) -- (503.34,237.64) .. controls (503.28,238.01) and (502.23,238.14) .. (501,237.94) .. controls (499.76,237.74) and (498.81,237.28) .. (498.87,236.91) -- (499.93,230.35) .. controls (499.99,229.98) and (501.04,229.85) .. (502.28,230.05) .. controls (503.51,230.25) and (504.47,230.71) .. (504.41,231.08) .. controls (504.35,231.45) and (503.3,231.59) .. (502.06,231.39) .. controls (500.83,231.19) and (499.87,230.72) .. (499.93,230.35) ;
                             		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ][fill={rgb, 255:red, 143; green, 133; blue, 13 }  ,fill opacity=1 ] (350.13,195.51) -- (353.22,201.39) .. controls (353.39,201.72) and (352.63,202.46) .. (351.53,203.04) .. controls (350.42,203.62) and (349.38,203.83) .. (349.2,203.49) -- (346.12,197.61) .. controls (345.94,197.28) and (346.7,196.54) .. (347.81,195.96) .. controls (348.92,195.38) and (349.96,195.17) .. (350.13,195.51) .. controls (350.31,195.84) and (349.55,196.58) .. (348.44,197.16) .. controls (347.33,197.74) and (346.29,197.95) .. (346.12,197.61) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ]   (397.33,181.9) -- (455.33,172.9) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ]   (479.33,176.9) -- (455.33,172.9) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ]   (465.33,156.9) -- (464.33,174.9) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ]   (433.83,143.4) -- (421.83,177.4) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ]   (420.83,151.9) -- (404.83,180.9) ;
                             		\\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.32 ] (435.33,201.15) .. controls (435.33,198.8) and (439.59,196.9) .. (444.83,196.9) .. controls (450.08,196.9) and (454.33,198.8) .. (454.33,201.15) .. controls (454.33,203.5) and (450.08,205.4) .. (444.83,205.4) .. controls (439.59,205.4) and (435.33,203.5) .. (435.33,201.15) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (485.73,154.31) -- (476.83,122.9) -- (478.33,108.9) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (483.33,153.4) -- (475.33,143.4) -- (469.83,119.4) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (481.33,155.4) -- (472.03,147.73) -- (465.33,131.4) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (477.83,157.9) -- (471.37,156.07) -- (460.83,141.4) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (484.7,197.07) -- (481.7,212.4) -- (483.83,161.9) -- cycle ;
                             		\\draw    (470.83,211.4) .. controls (482.4,211.4) and (483.24,215.01) .. (480.03,216.73) .. controls (476.83,218.46) and (470.83,217.66) .. (473.53,219.9) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (485.7,205.07) -- (490.7,217.07) -- (483.83,161.9) -- cycle ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.72 ]   (384.9,190.07) .. controls (394.3,186.73) and (398.63,164.73) .. (406.94,150.95) ;
                             		\\draw    (363.63,194.73) .. controls (426.3,204.73) and (346.63,184.73) .. (384.9,190.07) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (374.63,188.73) .. controls (395.03,166.07) and (393.63,158.73) .. (403.63,148.73) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (481.3,214.73) .. controls (487.63,200.07) and (479.97,183.4) .. (483.83,161.9) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (490.7,217.07) .. controls (492.63,208.07) and (484.3,187.4) .. (485.63,161.4) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ]   (452.97,126.4) .. controls (454.97,140.4) and (467.3,158.4) .. (479.97,157.73) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ]   (461.63,130.07) .. controls (462.63,137.73) and (470.3,157.07) .. (482.97,156.4) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (420.3,126.73) -- (400.97,145.07) -- (428.97,113.73) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (411.3,143.4) -- (421.3,129.4) -- (404.97,144.07) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (418.97,147.07) -- (430.97,136.73) -- (409.83,148.73) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (424.97,136.4) -- (435.63,122.73) -- (409.5,147.07) -- cycle ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ]   (440.97,124.73) .. controls (432.3,139.73) and (416.63,150.07) .. (409.83,148.73) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ]   (430.3,129.73) .. controls (419.63,141.73) and (412.97,148.07) .. (406.17,146.73) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (374.63,188.73) -- (387.63,178.07) -- (403.63,148.73) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.18 ] (360.3,192.73) -- (376.97,181.07) -- (399.97,147.4) -- cycle ;
                             		\\draw [color={rgb, 255:red, 146; green, 136; blue, 15 }  ,draw opacity=1 ][line width=1]    (393.33,142.05) .. controls (400.54,140.8) and (421.26,165.1) .. (402.66,150.1) .. controls (384.05,135.1) and (402.79,150.87) .. (403.28,156.68) .. controls (403.77,162.48) and (401.36,174.81) .. (412.23,165.82) ;
                             		\\draw [color={rgb, 255:red, 146; green, 136; blue, 15 }  ,draw opacity=1 ][line width=1]    (489.8,157.88) .. controls (484.05,157.13) and (467.53,171.67) .. (482.37,162.7) .. controls (497.2,153.73) and (482.26,163.16) .. (481.87,166.63) .. controls (481.48,170.1) and (483.4,177.48) .. (474.73,172.1) ;
                             		\\draw  [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ][dash pattern={on 0.84pt off 2.51pt}] (429.98,201.15) .. controls (429.98,197.15) and (436.63,193.9) .. (444.83,193.9) .. controls (453.03,193.9) and (459.68,197.15) .. (459.68,201.15) .. controls (459.68,205.15) and (453.03,208.4) .. (444.83,208.4) .. controls (436.63,208.4) and (429.98,205.15) .. (429.98,201.15) -- cycle ;
                             		\\draw [line width=1]    (92.67,218.33) -- (241.87,220.13) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.67,171.67) -- (299.87,173.47) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.67,171.67) -- (241.87,220.13) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.67,218.33) -- (299.87,173.47) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.67,171.67) -- (92.67,218.33) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (196.27,195.9) -- (195.87,61.47) ;
                             		\\draw [line width=1]    (241.87,220.13) -- (299.87,173.47) ;
                             		\\draw [line width=1]    (92.67,218.33) -- (195.87,61.47) ;
                             		\\draw [line width=1]    (195.87,61.47) -- (241.87,220.13) ;
                             		\\draw [line width=1]    (195.87,61.47) -- (299.87,173.47) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.67,171.67) -- (195.87,61.47) ;
                             		\\draw [line width=1]    (92.67,218.33) -- (51.13,226.07) ;
                             		\\draw [shift={(47.2,226.8)}, rotate = 349.45] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                             		\\draw [line width=1]    (241.87,220.13) -- (273.69,237.55) ;
                             		\\draw [shift={(277.2,239.47)}, rotate = 208.69] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                             		\\draw [line width=1]    (195.87,61.47) -- (196.44,36.13) ;
                             		\\draw [shift={(196.53,32.13)}, rotate = 91.3] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                             		\\draw (198.67,29) node [anchor=north west][inner sep=0.75pt]    {$z$};
                             		\\draw (269.33,215) node [anchor=north west][inner sep=0.75pt]    {$y$};
                             		\\draw (47.33,208) node [anchor=north west][inner sep=0.75pt]    {$x$};
                             		\\draw (184,200) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             		\\draw (300,165) node [anchor=north west][inner sep=0.75pt]    {$D$};
                             		\\draw (228,222) node [anchor=north west][inner sep=0.75pt]    {$C$};
                             		\\draw (84,222) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             		\\draw (130,161) node [anchor=north west][inner sep=0.75pt]    {$A$};
                             		\\draw (179.33,45.67) node [anchor=north west][inner sep=0.75pt]    {$S$};
                             	\\end{tikzpicture}}
                             \\end{center}''' % (latex(l), latex(CD_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $C(0;%s;0); D(-%s;0;0)$' % (latex(a), latex(a))
            nb_da_1_s = '$C(%s;0;0); D(0;-%s;0)$' % (latex(a), latex(a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Do $ABCD$ là hình vuông tâm $O$, $CD = %s \\Rightarrow OB = OC = \\frac{CD}{\\sqrt{2}} = %s$. \\\\
            Vì tia $Oy$ chứa $OC$, tia $Ox$ chứa $OB$, và $D$ đối xứng với $B$ qua $O$ nên $C(0;%s;0)$ và $D(-%s;0;0)$.'''
                % (latex(CD_val), latex(a), latex(a), latex(a)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Tính toán
            y_I = a / 2
            z_I = h / 2
            R2_true = l**2 / 4
            R2_false = l**2

            # Các đáp án
            th_da_1_d = '\\True Phương trình mặt cầu đường kính $SC$ là $x^2 + \\left(y - %s\\right)^2 + \\left(z - %s\\right)^2 = %s$' % (latex(y_I), latex(z_I), latex(R2_true))
            th_da_1_s = 'Phương trình mặt cầu đường kính $SC$ là $x^2 + \\left(y - %s\\right)^2 + \\left(z - %s\\right)^2 = %s$' % (latex(y_I), latex(z_I), latex(R2_false))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $S \\in Oz \\Rightarrow S(0;0;z_S)$. \\\\
            $OS = \\sqrt{SB^2 - OB^2} = \\sqrt{%s^2 - %s^2} = %s \\Rightarrow S(0;0;%s)$. \\\\
            Trung điểm $I$ của $SC$ là $I\\left(0; %s; %s\\right)$. \\\\
            Mặt cầu đường kính $SC$ có tâm $I$, bán kính $R = \\frac{SC}{2} = \\frac{\\sqrt{0^2 + %s^2 + %s^2}}{2} = %s$. \\\\
            Phương trình mặt cầu đường kính $SC$ là $x^2 + \\left(y - %s\\right)^2 + \\left(z - %s\\right)^2 = %s$.'''
                % (latex(l), latex(a), latex(h), latex(h),
                   latex(y_I), latex(z_I),
                   latex(a), latex(h), latex(l/2),
                   latex(y_I), latex(z_I), latex(R2_true)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Tính toán
            BM_true = sqrt(9*a**2 + h**2) / 2
            BM_false = sqrt(a**2 + h**2) / 2

            # Các đáp án
            vd_da_1_d = '\\True Gọi $M$ là trung điểm cạnh $SD$ thì $BM = %s$' % (latex(BM_true))
            vd_da_1_s = 'Gọi $M$ là trung điểm cạnh $SD$ thì $BM = %s$' % (latex(BM_false))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $S(0;0;%s), D(-%s;0;0) \\Rightarrow M\\left(%s; 0; %s\\right)$. \\\\
            Điểm $B(%s;0;0)$. \\\\
            $\\overrightarrow{BM} = \\left(%s; 0; %s\\right) \\Rightarrow BM = \\sqrt{\\left(%s\\right)^2 + 0^2 + \\left(%s\\right)^2} = %s$.'''
                % (latex(h), latex(a), latex(-a/2), latex(h/2),
                   latex(a),
                   latex(-3*a/2), latex(h/2),
                   latex(-3*a/2), latex(h/2), latex(BM_true)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Tính toán
            E_x_true = -a / 2
            E_z_true = h / 2
            E_x_false = a / 2

            # Các đáp án
            vdc_da_1_d = '\\True Gọi $G$ là trọng tâm tam giác $SCD$. Nếu chi đoàn muốn treo hệ thống đèn led trang trí nối từ một điểm $E$ trên mặt phẳng $(SBD)$ đến hai điểm $G, A$ sao cho $\\left| EG - EA \\right|$ là lớn nhất thì $E\\left(%s; 0; %s\\right)$' % (latex(E_x_true), latex(E_z_true))
            vdc_da_1_s = 'Gọi $G$ là trọng tâm tam giác $SCD$. Nếu chi đoàn muốn treo hệ thống đèn led trang trí nối từ một điểm $E$ trên mặt phẳng $(SBD)$ đến hai điểm $G, A$ sao cho $\\left| EG - EA \\right|$ là lớn nhất thì $E\\left(%s; 0; %s\\right)$' % (latex(E_x_false), latex(E_z_true))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Phương trình tham số của GC
            t = symbols('t')
            x_eq = -a/3 * t
            y_eq = a - 2*a/3 * t
            z_eq = h/3 * t

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Mặt phẳng $(SBD)$ có phương trình $y=0$. \\\\
            Điểm $A$ đối xứng với $C(0;%s;0)$ qua tâm $O$ nên $A(0;-%s;0)$. \\\\
            Hình chiếu của $A$ trên $(SBD)$ là $O$, suy ra điểm đối xứng với $A$ qua mặt phẳng $(SBD)$ là $C(0;%s;0)$. \\\\
            Vì $E \\in (SBD)$ nên $EA = EC$. Do đó $\\left| EG - EA \\right| = \\left| EG - EC \\right| \\le GC$. \\\\
            Dấu bằng xảy ra khi $E, G, C$ thẳng hàng và $G$ nằm giữa $E$ và $C$. \\\\
            Tọa độ trọng tâm $G$ của tam giác $SCD$ là:\\\\ $x_G = \\frac{0 + 0 + (-%s)}{3} = %s$, $y_G = \\frac{%s + 0 + 0}{3} = %s$, $z_G = \\frac{0 + 0 + %s}{3} = %s \\\\ \\Rightarrow G\\left(%s; %s; %s\\right)$ và
            $\\overrightarrow{CG} = \\left(%s; %s; %s\\right)$. \\\\
            Đường thẳng $GC$ có phương trình tham số: $\\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases}$. \\\\
            Điểm $E = GC \\cap (SBD) \\Rightarrow y_E = 0 \\Rightarrow %s = 0 \\Leftrightarrow t = \\frac{3}{2}$. \\\\
            Suy ra $x_E = %s \\cdot \\frac{3}{2} = %s$, $z_E = %s \\cdot \\frac{3}{2} = %s$. Vậy $E\\left(%s; 0; %s\\right)$.'''
                % (
                    latex(a), latex(a), latex(a),
                    latex(a), latex(-a/3), latex(a), latex(a/3), latex(h), latex(h/3), latex(-a/3), latex(a/3), latex(h/3),
                    latex(-a/3), latex(-2*a/3), latex(h/3),
                    latex(x_eq), latex(y_eq), latex(z_eq),
                    latex(y_eq),
                    latex(-a/3), latex(E_x_true), latex(h/3), latex(E_z_true), latex(E_x_true), latex(E_z_true)
                ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

