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


def bt_dang11_p3_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vận tốc v (km/s) và thời gian t (phút) sao cho quãng đường và bán kính tạo thành bộ số Pytago đẹp
                # Các bộ (v, t, S, OB, h) được tính sẵn với OA = 6400
                data_list = [
                    (8, 10, 4800, 8000, 1600),
                    (10, 8, 4800, 8000, 1600),
                    (4, 20, 4800, 8000, 1600),
                    (5, 16, 4800, 8000, 1600),
                    (10, 20, 12000, 13600, 7200),
                    (20, 10, 12000, 13600, 7200),
                    (8, 25, 12000, 13600, 7200)
                ]

                v, t, S, OB, kq = random.choice(data_list)

                # Các đáp án trắc nghiệm
                da = str(kq)

                # Tạo các phương án nhiễu sai khác nhau
                s_set = set()
                while len(s_set) < 3:
                    offset = random.choice([200, -200, 400, -400, 600, -600, 800, -800, 1200])
                    wrong_val = kq + offset
                    if wrong_val > 0 and wrong_val != kq:
                        s_set.add(str(wrong_val))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 10; green, 107; blue, 220 }  ,fill opacity=1 ] (370.7,122.83) .. controls (370.7,87.61) and (399.25,59.06) .. (434.47,59.06) .. controls (469.69,59.06) and (498.24,87.61) .. (498.24,122.83) .. controls (498.24,158.05) and (469.69,186.6) .. (434.47,186.6) .. controls (399.25,186.6) and (370.7,158.05) .. (370.7,122.83) -- cycle ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (409.77,97.68) .. controls (409.77,97.68) and (409.77,97.68) .. (409.77,97.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (396.3,85.71) .. controls (394.8,89.2) and (393.3,92.69) .. (391.81,96.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (393.05,98.18) .. controls (400.08,91.37) and (402.04,86.02) .. (402.04,94.19) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (403.03,96.43) .. controls (401.46,97.76) and (397.09,99.22) .. (398.54,100.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (402.04,100.67) .. controls (402.04,100.67) and (402.04,100.67) .. (402.04,100.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (406.28,99.93) .. controls (407.28,97.76) and (410.09,95.68) .. (409.27,93.44) .. controls (408.04,90.06) and (404.15,88.38) .. (401.29,86.2) .. controls (400.48,85.59) and (402.45,87.87) .. (403.03,88.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (397.05,81.71) .. controls (397.88,81.21) and (398.71,80.72) .. (399.54,80.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (397.55,80.22) .. controls (396.63,79.88) and (395.72,79.55) .. (394.8,79.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (393.55,83.46) .. controls (392.89,82.79) and (392.22,82.13) .. (391.56,81.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (391.81,85.71) .. controls (390.89,86.04) and (389.98,86.37) .. (389.06,86.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (389.56,89.7) .. controls (388.9,90.03) and (388.23,90.36) .. (387.57,90.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (388.06,93.69) .. controls (387.07,94.02) and (386.07,94.35) .. (385.07,94.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (385.82,96.18) .. controls (384.65,96.85) and (383.49,97.51) .. (382.33,98.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (383.32,98.68) .. controls (383.24,99.43) and (383.16,100.18) .. (383.07,100.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (388.06,98.68) .. controls (388.06,100.09) and (388.06,101.51) .. (388.06,102.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (391.06,101.42) .. controls (391.47,101.84) and (391.89,102.25) .. (392.31,102.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (394.55,102.42) .. controls (394.88,102.42) and (395.22,102.42) .. (395.55,102.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (385.82,105.66) .. controls (386.4,105.91) and (386.98,106.16) .. (387.57,106.41) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (424.99,147.08) .. controls (422.83,143.75) and (420.67,140.43) .. (418.5,137.1) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (418.5,136.35) .. controls (417.01,133.61) and (415.51,130.86) .. (414.01,128.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (421,149.08) .. controls (417.59,143.84) and (414.18,138.6) .. (410.77,133.36) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (413.01,146.33) .. controls (411.68,144.09) and (410.35,141.84) .. (409.02,139.6) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (430.48,146.08) .. controls (426.99,140.26) and (423.49,134.44) .. (420,128.62) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (434.47,151.57) .. controls (435.55,148.24) and (436.63,144.92) .. (437.71,141.59) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (436.97,144.59) .. controls (434.22,140.59) and (431.48,136.6) .. (428.73,132.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (436.97,142.59) .. controls (438.13,142.92) and (439.29,143.25) .. (440.46,143.59) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (438.96,146.58) .. controls (438.96,147.25) and (438.96,147.91) .. (438.96,148.58) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (437.71,151.57) .. controls (437.71,152.07) and (437.71,152.57) .. (437.71,153.07) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (433.47,153.57) .. controls (432.97,154.32) and (432.47,155.06) .. (431.98,155.81) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (429.98,155.81) .. controls (430.15,156.98) and (430.31,158.14) .. (430.48,159.31) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (427.73,160.55) .. controls (428.32,160.72) and (428.9,160.89) .. (429.48,161.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (424.49,162.05) .. controls (424.91,162.88) and (425.32,163.71) .. (425.74,164.54) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (424.74,164.54) .. controls (424.49,165.46) and (424.24,166.37) .. (423.99,167.29) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (421,166.79) .. controls (421,167.62) and (421,168.45) .. (421,169.29) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (420.25,165.29) .. controls (420.25,160.39) and (420.25,155.48) .. (420.25,150.57) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (423.24,157.06) .. controls (424.88,154.3) and (426.19,150.92) .. (428.98,149.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (421.5,152.82) .. controls (420.25,151.82) and (419,150.82) .. (417.75,149.82) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (475.89,108.66) .. controls (471.52,113.02) and (467.17,117.41) .. (462.66,121.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (462.91,119.14) .. controls (462.26,117.4) and (461.33,115.41) .. (461.91,113.65) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (462.91,111.9) .. controls (464.41,110.4) and (465.91,108.91) .. (467.4,107.41) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (468.15,106.66) .. controls (470.23,105.91) and (472.31,105.17) .. (474.39,104.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (475.89,106.16) .. controls (477.22,107.08) and (478.55,107.99) .. (479.88,108.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (482.87,110.9) .. controls (484.29,110.82) and (485.7,110.74) .. (487.11,110.65) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (488.11,110.65) .. controls (489.36,109.99) and (490.61,109.32) .. (491.85,108.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (492.35,108.91) .. controls (492.27,112.82) and (492.19,116.73) .. (492.1,120.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (493.85,116.14) .. controls (493.1,123.05) and (492.35,129.95) .. (491.6,136.85) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (489.11,120.38) .. controls (487.2,118.14) and (486.01,114.97) .. (483.37,113.65) .. controls (480.92,112.42) and (475.48,110.67) .. (475.14,113.4) .. controls (474.9,115.29) and (484.8,123.8) .. (487.11,125.87) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (482.87,120.63) .. controls (481.96,122.63) and (481.04,124.63) .. (480.13,126.62) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (478.38,125.37) .. controls (476.18,122.76) and (473.77,120.23) .. (470.9,118.39) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (469.9,119.39) .. controls (470.31,121.38) and (470.73,123.38) .. (471.15,125.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (466.16,123.13) .. controls (466.49,124.54) and (466.82,125.96) .. (467.15,127.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (485.12,126.62) .. controls (484.95,128.95) and (484.78,131.28) .. (484.62,133.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (489.11,133.86) .. controls (488.53,134.77) and (487.94,135.69) .. (487.36,136.6) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (485.37,125.87) .. controls (486.28,126.95) and (487.2,128.04) .. (488.11,129.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (491.35,140.09) .. controls (491.02,141.34) and (490.69,142.59) .. (490.36,143.84) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (489.11,141.09) .. controls (489.03,141.51) and (488.94,141.92) .. (488.86,142.34) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (488.86,142.59) .. controls (488.19,145) and (487.53,147.41) .. (486.86,149.82) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (479.63,88.45) .. controls (480.04,88.2) and (480.46,87.95) .. (480.88,87.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (481.62,88.95) .. controls (481.71,89.03) and (481.79,89.11) .. (481.87,89.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (476.88,88.7) .. controls (475.47,88.7) and (474.06,88.7) .. (472.64,88.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=5.25] [line join = round][line cap = round] (435.97,69.99) .. controls (435.55,69.74) and (435.14,69.49) .. (434.72,69.24) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (400.04,78.22) .. controls (401.29,77.97) and (402.54,77.72) .. (403.78,77.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (402.54,79.72) .. controls (402.95,79.38) and (403.37,79.05) .. (403.78,78.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.55,76.47) .. controls (396.88,76.47) and (397.21,76.47) .. (397.55,76.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (398.04,76.97) .. controls (397.96,76.56) and (397.88,76.14) .. (397.79,75.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (404.03,77.72) .. controls (405.86,76.97) and (407.69,76.22) .. (409.52,75.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (406.28,78.72) .. controls (407.11,78.05) and (407.94,77.39) .. (408.77,76.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (405.53,78.22) .. controls (404.53,79.38) and (403.53,80.55) .. (402.54,81.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (378.83,100.67) .. controls (379.25,103.34) and (379.67,106) .. (380.08,108.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (397.05,105.66) .. controls (398.71,105.33) and (400.37,105) .. (402.04,104.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (402.04,105.42) .. controls (402.54,105.58) and (403.03,105.75) .. (403.53,105.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (405.53,103.67) .. controls (405.11,104.33) and (404.7,105) .. (404.28,105.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (404.28,105.17) .. controls (404.7,106.75) and (405.11,108.33) .. (405.53,109.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (391.06,106.66) .. controls (390.73,108.74) and (390.39,110.82) .. (390.06,112.9) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.32,109.16) .. controls (388.15,110.9) and (388.98,112.65) .. (389.81,114.4) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.57,109.91) .. controls (388.06,111.65) and (388.56,113.4) .. (389.06,115.15) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (385.82,109.66) .. controls (386.32,110.99) and (386.82,112.32) .. (387.32,113.65) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (385.32,109.91) .. controls (386.15,111.65) and (386.98,113.4) .. (387.82,115.15) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (392.56,105.17) .. controls (392.22,106.16) and (391.89,107.16) .. (391.56,108.16) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (388.56,109.66) .. controls (388.73,110.32) and (388.9,110.99) .. (389.06,111.65) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (385.07,112.15) .. controls (387.07,113.98) and (389.06,115.81) .. (391.06,117.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (386.32,114.9) .. controls (387.9,115.73) and (389.48,116.56) .. (391.06,117.39) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (390.56,113.65) .. controls (392.31,115.48) and (394.05,117.31) .. (395.8,119.14) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (392.06,116.89) .. controls (393.05,117.81) and (394.05,118.72) .. (395.05,119.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (391.06,115.15) .. controls (392.72,116.31) and (394.03,118.85) .. (396.05,118.64) .. controls (397.64,118.47) and (397.55,115.81) .. (398.29,114.4) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.55,117.14) .. controls (396.71,116.64) and (396.88,116.14) .. (397.05,115.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.55,119.64) .. controls (397.88,120.63) and (399.21,121.63) .. (400.54,122.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (397.79,120.63) .. controls (399.04,120.72) and (400.29,120.8) .. (401.54,120.88) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (401.54,122.13) .. controls (401.54,123.13) and (401.54,124.13) .. (401.54,125.13) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (402.04,124.88) .. controls (403.03,125.21) and (404.03,125.54) .. (405.03,125.87) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (406.03,126.62) .. controls (407.61,127.87) and (409.19,129.12) .. (410.77,130.36) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (407.77,128.62) .. controls (407.77,129.28) and (407.77,129.95) .. (407.77,130.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (408.52,127.62) .. controls (409.94,126.54) and (411.35,125.46) .. (412.76,124.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (415.26,125.13) .. controls (416.67,124.88) and (418.09,124.63) .. (419.5,124.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (423.99,129.37) .. controls (424.99,129.37) and (425.99,129.37) .. (426.99,129.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (439.96,139.6) .. controls (441.8,141.44) and (445.25,144.07) .. (443.95,146.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (442.95,139.85) .. controls (443.95,140.93) and (444.95,142.01) .. (445.95,143.09) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (443.45,142.59) .. controls (442.95,141.59) and (442.45,140.59) .. (441.96,139.6) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (441.96,151.57) .. controls (441.21,152.65) and (440.46,153.73) .. (439.71,154.81) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (434.22,160.55) .. controls (434.05,161.38) and (433.89,162.22) .. (433.72,163.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (423.49,170.28) .. controls (424.32,170.95) and (425.16,171.61) .. (425.99,172.28) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (426.74,167.29) .. controls (427.73,167.62) and (428.73,167.95) .. (429.73,168.29) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (428.23,167.29) .. controls (429.15,166.21) and (430.06,165.13) .. (430.98,164.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.5,169.78) .. controls (418.75,172.03) and (420,174.28) .. (421.25,176.52) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (421.25,173.28) .. controls (421.5,174.03) and (421.75,174.77) .. (422,175.52) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (421,176.52) .. controls (422.25,178.1) and (423.49,179.68) .. (424.74,181.26) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (408.77,75.73) .. controls (409.94,75.39) and (411.1,75.06) .. (412.27,74.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (412.02,75.73) .. controls (411.68,74.56) and (411.35,73.4) .. (411.02,72.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (411.02,71.73) .. controls (413.76,71.65) and (416.51,71.57) .. (419.25,71.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.01,71.73) .. controls (416.59,72.57) and (416.17,73.4) .. (415.76,74.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (418,71.48) .. controls (419.75,72.48) and (421.5,73.48) .. (423.24,74.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (420.25,73.48) .. controls (420.58,74.89) and (420.91,76.31) .. (421.25,77.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (421,75.23) .. controls (420.91,76.06) and (420.83,76.89) .. (420.75,77.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (420.25,75.73) .. controls (419.5,76.31) and (418.75,76.89) .. (418,77.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (418.75,76.72) .. controls (419.58,77.14) and (420.42,77.56) .. (421.25,77.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (401.79,72.73) .. controls (402.45,73.15) and (403.12,73.56) .. (403.78,73.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (404.03,73.98) .. controls (405.28,73.48) and (406.53,72.98) .. (407.77,72.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (405.03,72.73) .. controls (404.78,72.15) and (404.53,71.57) .. (404.28,70.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (403.78,71.73) .. controls (403.53,71.9) and (403.28,72.07) .. (403.03,72.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (408.52,69.99) .. controls (409.02,69.82) and (409.52,69.65) .. (410.02,69.49) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (413.01,69.24) .. controls (413.43,68.91) and (413.85,68.57) .. (414.26,68.24) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.26,69.24) .. controls (418.34,68.82) and (419.42,68.41) .. (420.5,67.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (419.75,67.74) .. controls (419.25,67.41) and (418.75,67.08) .. (418.25,66.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (420.5,67.74) .. controls (421.75,66.99) and (422.99,66.24) .. (424.24,65.5) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (422.25,66.74) .. controls (424.24,66.33) and (426.24,65.91) .. (428.23,65.5) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (423.99,65.25) .. controls (423.49,65.25) and (422.99,65.25) .. (422.49,65.25) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (405.78,84.71) .. controls (407.03,85.54) and (408.27,86.37) .. (409.52,87.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (395.8,74.73) .. controls (398.04,75.31) and (400.29,75.89) .. (402.54,76.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (403.03,76.47) .. controls (404.95,75.89) and (406.86,75.31) .. (408.77,74.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (412.27,91.94) .. controls (414.93,88.72) and (416.87,84.26) .. (420.75,82.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (418.25,82.21) .. controls (417.92,81.38) and (417.59,80.55) .. (417.26,79.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.01,79.22) .. controls (416.26,81.05) and (415.51,82.88) .. (414.76,84.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (414.26,82.96) .. controls (414.26,84.04) and (414.26,85.12) .. (414.26,86.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (414.26,86.2) .. controls (414.26,86.37) and (414.26,86.54) .. (414.26,86.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (414.51,84.46) .. controls (413.35,85.87) and (412.18,87.29) .. (411.02,88.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (412.02,90.2) .. controls (413.7,87.17) and (419.2,83.41) .. (416.76,80.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (415.76,80.72) .. controls (415.34,81.21) and (414.93,81.71) .. (414.51,82.21) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (413.76,85.71) .. controls (413.43,86.37) and (413.1,87.04) .. (412.76,87.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (420,83.46) .. controls (421.12,82.74) and (423.29,82.58) .. (423.99,83.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (423.74,83.71) .. controls (424.74,84.79) and (425.74,85.87) .. (426.74,86.95) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (426.99,88.2) .. controls (426.65,89.03) and (426.32,89.86) .. (425.99,90.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (426.74,88.7) .. controls (426.8,89.37) and (426.31,90.79) .. (425.74,90.45) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (425.24,90.2) .. controls (425.49,89.03) and (425.74,87.87) .. (425.99,86.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (424.49,86.7) .. controls (422.08,87.2) and (419.67,87.7) .. (417.26,88.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (418,86.7) .. controls (420,85.95) and (422,85.21) .. (423.99,84.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (422.49,84.71) .. controls (421.25,85.29) and (420,85.87) .. (418.75,86.45) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (419.25,85.21) .. controls (420.17,83.96) and (421.08,82.71) .. (422,81.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (416.51,88.45) .. controls (416.51,88.45) and (416.51,88.45) .. (416.51,88.45) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.5,88.2) .. controls (418.34,89.61) and (419.17,91.03) .. (420,92.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (418,90.2) .. controls (417.59,91.03) and (417.17,91.86) .. (416.76,92.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (416.76,88.95) .. controls (416.01,90.94) and (415.26,92.94) .. (414.51,94.94) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (415.01,89.95) .. controls (414.68,92.03) and (414.34,94.1) .. (414.01,96.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (417.75,92.19) .. controls (418.59,92.86) and (419.42,93.52) .. (420.25,94.19) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (420.25,93.44) .. controls (420.75,93.19) and (421.25,92.94) .. (421.75,92.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (424.49,68.74) .. controls (428.65,67.49) and (432.81,66.24) .. (436.97,65) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (436.97,65) .. controls (440.79,65.58) and (444.62,66.16) .. (448.44,66.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (437.96,65.75) .. controls (440.65,66.67) and (443.44,68.68) .. (446.2,67.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (439.96,67.49) .. controls (442.29,68.16) and (444.62,68.82) .. (446.94,69.49) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (438.96,66.74) .. controls (440.96,68.07) and (442.95,69.4) .. (444.95,70.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (440.21,67.49) .. controls (440.04,69.9) and (439.88,72.32) .. (439.71,74.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (439.96,73.73) .. controls (441.87,73.23) and (443.78,72.73) .. (445.7,72.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (442.95,71.73) .. controls (442.62,71.07) and (442.29,70.4) .. (441.96,69.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (441.71,71.73) .. controls (440.21,69.74) and (438.71,67.74) .. (437.21,65.75) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (430.48,67.99) .. controls (430.15,68.24) and (429.81,68.49) .. (429.48,68.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (429.23,69.49) .. controls (429.9,70.57) and (430.56,71.65) .. (431.23,72.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (430.73,69.99) .. controls (431.39,70.99) and (432.06,71.98) .. (432.72,72.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (427.98,68.74) .. controls (430.06,71.32) and (432.14,73.9) .. (434.22,76.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (431.48,73.73) .. controls (431.89,75.39) and (432.31,77.06) .. (432.72,78.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (434.22,73.23) .. controls (435.14,73.73) and (436.05,74.23) .. (436.97,74.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (438.96,71.73) .. controls (438.79,72.9) and (438.63,74.06) .. (438.46,75.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (438.71,74.73) .. controls (437.21,76.14) and (435.72,77.56) .. (434.22,78.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (436.97,73.48) .. controls (436.22,74.56) and (435.47,75.64) .. (434.72,76.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (431.23,73.73) .. controls (431.14,74.56) and (431.06,75.39) .. (430.98,76.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (434.22,73.23) .. controls (434.14,74.98) and (434.05,76.72) .. (433.97,78.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (430.98,74.73) .. controls (431.64,76.14) and (432.31,77.56) .. (432.97,78.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (430.73,76.72) .. controls (431.81,78.05) and (432.89,79.38) .. (433.97,80.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (469.15,88.2) .. controls (468.23,89.03) and (467.32,89.86) .. (466.41,90.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (467.4,91.44) .. controls (467.9,92.52) and (468.4,93.61) .. (468.9,94.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (468.65,90.7) .. controls (469.4,91.69) and (470.15,92.69) .. (470.9,93.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (473.64,92.94) .. controls (471.64,94.19) and (469.65,95.44) .. (467.65,96.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (468.9,93.69) .. controls (467.9,94.35) and (466.9,95.02) .. (465.91,95.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (466.41,94.69) .. controls (464.99,94.6) and (463.58,94.52) .. (462.16,94.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (462.16,94.94) .. controls (462.75,96.43) and (463.33,97.93) .. (463.91,99.43) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (464.91,99.68) .. controls (466.24,98.68) and (467.57,97.68) .. (468.9,96.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (466.9,98.68) .. controls (466.49,98.18) and (466.07,97.68) .. (465.66,97.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (464.66,97.18) .. controls (465.34,96.7) and (466.65,96.26) .. (467.15,96.93) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (466.16,97.43) .. controls (467.15,96.52) and (468.15,95.6) .. (469.15,94.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (476.88,84.21) .. controls (477.47,83.46) and (478.05,82.71) .. (478.63,81.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (478.63,81.71) .. controls (478.71,81.21) and (478.8,80.72) .. (478.88,80.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (480.13,80.72) .. controls (480.96,82.05) and (481.79,83.38) .. (482.62,84.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (480.63,83.71) .. controls (481.04,84.46) and (481.46,85.21) .. (481.87,85.95) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (482.87,83.46) .. controls (484.7,86.54) and (486.53,89.61) .. (488.36,92.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (484.62,88.2) .. controls (486.36,90.86) and (488.11,93.52) .. (489.86,96.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (488.11,91.69) .. controls (489.19,93.86) and (490.27,96.02) .. (491.35,98.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (486.36,93.44) .. controls (487.2,95.02) and (488.03,96.6) .. (488.86,98.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (485.62,90.94) .. controls (485.45,92.52) and (485.28,94.1) .. (485.12,95.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (481.87,91.69) .. controls (484.22,95.34) and (484.74,96.42) .. (483.87,94.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (476.63,92.44) .. controls (477.8,94.1) and (478.96,95.77) .. (480.13,97.43) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (476.63,93.69) .. controls (476.88,94.27) and (477.13,94.85) .. (477.38,95.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (476.14,93.19) .. controls (477.38,94.6) and (478.63,96.02) .. (479.88,97.43) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (477.88,96.18) .. controls (478.38,96.43) and (478.88,96.68) .. (479.38,96.93) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (478.63,95.68) .. controls (476.97,95.02) and (475.3,94.35) .. (473.64,93.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (485.62,106.41) .. controls (486.12,105.5) and (486.61,104.58) .. (487.11,103.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (486.86,107.16) .. controls (487.94,106.41) and (489.03,105.66) .. (490.11,104.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (487.86,103.92) .. controls (489.36,104.5) and (490.86,105.08) .. (492.35,105.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (490.36,104.92) .. controls (494.21,103.38) and (495.05,104.37) .. (493.85,103.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (494.85,105.91) .. controls (494.51,105) and (494.18,104.08) .. (493.85,103.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (492.35,99.43) .. controls (492.93,100.51) and (493.52,101.59) .. (494.1,102.67) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (483.87,151.32) .. controls (484.54,152.99) and (485.2,154.65) .. (485.87,156.31) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (491.72,146.64) .. controls (490.31,149.76) and (488.91,152.88) .. (487.5,156.01) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (486.12,154.32) .. controls (485.7,156.39) and (485.28,158.47) .. (484.87,160.55) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (485.62,157.06) .. controls (485.62,158.22) and (485.62,159.39) .. (485.62,160.55) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (476.63,76.47) .. controls (474.97,74.98) and (473.31,73.48) .. (471.64,71.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (471.4,71.48) .. controls (470.56,71.9) and (469.73,72.32) .. (468.9,72.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (468.65,73.48) .. controls (467.82,75.23) and (466.99,76.97) .. (466.16,78.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (466.16,78.72) .. controls (467.07,79.55) and (467.99,80.38) .. (468.9,81.21) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (468.9,81.21) .. controls (470.23,81.13) and (471.56,81.05) .. (472.89,80.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (472.89,80.72) .. controls (472.39,78.3) and (471.89,75.89) .. (471.4,73.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (470.9,73.73) .. controls (470.65,75.56) and (470.4,77.39) .. (470.15,79.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (469.9,74.73) .. controls (469.48,76.22) and (469.07,77.72) .. (468.65,79.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (468.9,79.22) .. controls (469.73,79.47) and (470.56,79.72) .. (471.4,79.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (473.39,75.48) .. controls (474.89,76.81) and (476.39,78.14) .. (477.88,79.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (470.9,78.22) .. controls (470.65,78.64) and (470.4,79.05) .. (470.15,79.47) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (467.9,78.47) .. controls (468.23,78.89) and (468.57,79.3) .. (468.9,79.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (472.89,81.96) .. controls (472.81,82.21) and (472.73,82.46) .. (472.64,82.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (460.92,81.46) .. controls (462.66,82.96) and (464.41,84.46) .. (466.16,85.95) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (461.91,82.46) .. controls (460.83,82.96) and (459.75,83.46) .. (458.67,83.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (458.67,84.46) .. controls (458.75,85.21) and (458.84,85.95) .. (458.92,86.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (459.42,86.7) .. controls (460.42,85.71) and (461.42,84.71) .. (462.41,83.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (462.91,84.46) .. controls (463.74,85.12) and (464.58,85.79) .. (465.41,86.45) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (465.41,86.7) .. controls (464.91,87.04) and (464.41,87.37) .. (463.91,87.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (407.28,114.4) .. controls (409.19,114.4) and (411.1,114.4) .. (413.01,114.4) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (411.02,114.9) .. controls (412.51,115.15) and (414.01,115.39) .. (415.51,115.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (411.02,114.9) .. controls (410.85,114.9) and (410.69,114.9) .. (410.52,114.9) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (419,115.89) .. controls (419.08,115.89) and (419.17,115.89) .. (419.25,115.89) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (406.53,116.39) .. controls (406.69,116.39) and (406.86,116.39) .. (407.03,116.39) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (403.03,91.69) .. controls (406.53,91.94) and (410.02,92.19) .. (413.51,92.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (420,85.95) .. controls (421.08,85.87) and (422.16,85.79) .. (423.24,85.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (401.79,100.67) .. controls (402.29,101.42) and (402.78,102.17) .. (403.28,102.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (472.89,92.19) .. controls (473.89,92.36) and (474.89,92.52) .. (475.89,92.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (466.65,96.18) .. controls (466.07,96.1) and (465.49,96.02) .. (464.91,95.93) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (469.4,76.72) .. controls (468.9,76.72) and (468.4,76.72) .. (467.9,76.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (469.4,76.97) .. controls (469.82,76.64) and (470.23,76.31) .. (470.65,75.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (483.62,89.7) .. controls (484.12,90.61) and (484.62,91.53) .. (485.12,92.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (494.1,121.13) .. controls (494.27,123.46) and (494.43,125.79) .. (494.6,128.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (493.85,130.61) .. controls (493.77,132.44) and (493.68,134.27) .. (493.6,136.1) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (392.78,120.77) .. controls (384.96,105.5) and (393.89,85.3) .. (412.72,75.65) .. controls (431.56,66) and (453.17,70.55) .. (460.99,85.82) .. controls (468.81,101.09) and (459.89,121.29) .. (441.05,130.94) .. controls (422.21,140.59) and (400.6,136.04) .. (392.78,120.77) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (377.85,140.43) .. controls (364.5,114.38) and (377.58,81.02) .. (407.05,65.92) .. controls (436.52,50.82) and (471.24,59.7) .. (484.58,85.75) .. controls (497.93,111.8) and (484.86,145.16) .. (455.39,160.26) .. controls (425.91,175.36) and (391.2,166.49) .. (377.85,140.43) -- cycle ;
            	\draw  [line width=0.75]  (370.7,122.83) .. controls (370.7,87.61) and (399.25,59.06) .. (434.47,59.06) .. controls (469.69,59.06) and (498.24,87.61) .. (498.24,122.83) .. controls (498.24,158.05) and (469.69,186.6) .. (434.47,186.6) .. controls (399.25,186.6) and (370.7,158.05) .. (370.7,122.83) -- cycle ;
            	\draw  [draw opacity=0] (497.66,117.64) .. controls (522.24,136.62) and (535.35,156.59) .. (529.28,169.67) .. controls (520.13,189.4) and (470.76,185.94) .. (419.02,161.93) .. controls (367.28,137.93) and (332.76,102.47) .. (341.92,82.73) .. controls (347.71,70.24) and (369.62,67.05) .. (398.05,72.47) -- (435.6,126.2) -- cycle ; \draw   (497.66,117.64) .. controls (522.24,136.62) and (535.35,156.59) .. (529.28,169.67) .. controls (520.13,189.4) and (470.76,185.94) .. (419.02,161.93) .. controls (367.28,137.93) and (332.76,102.47) .. (341.92,82.73) .. controls (347.71,70.24) and (369.62,67.05) .. (398.05,72.47) ;  
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (339.79,86.95) -- (335.1,110.04) -- (334.04,109.83) -- (338.73,86.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (348.27,101.13) -- (324.83,103.71) -- (327.16,90.6) -- (350.6,88.02) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (349.58,91.93) -- (326.86,94.56) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (348.93,96.19) -- (326.2,98.82) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (339,89.4) -- (336.43,102.33) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (344.58,88.82) -- (342.01,101.74) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (332.71,90.1) -- (330.14,103.03) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (345.49,116.89) -- (322.04,119.47) -- (324.37,106.37) -- (347.82,103.79) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (346.8,107.69) -- (324.08,110.32) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (346.14,111.95) -- (323.42,114.58) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (336.22,105.17) -- (333.65,118.09) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (341.8,104.58) -- (339.23,117.5) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (329.93,105.87) -- (327.35,118.79) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (326.87,82.91) -- (322.66,79.06) -- (327,70.08) -- (332.62,70.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (322.66,79.06) .. controls (321.87,78.68) and (322.19,76.36) .. (323.39,73.88) .. controls (324.59,71.4) and (326.2,69.7) .. (327,70.08) .. controls (327.79,70.47) and (327.47,72.79) .. (326.27,75.27) .. controls (325.07,77.75) and (323.46,79.45) .. (322.66,79.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (327.42,82.8) -- (322.78,78.48) -- (322.84,76.8) -- (327.48,81.12) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (324.95,82.64) .. controls (324.12,82.23) and (324.93,78.83) .. (326.76,75.03) .. controls (328.59,71.24) and (330.75,68.49) .. (331.58,68.89) .. controls (332.42,69.29) and (331.61,72.7) .. (329.78,76.49) .. controls (327.95,80.29) and (325.79,83.04) .. (324.95,82.64) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (324.95,82.64) -- (331.58,68.89) -- (336.5,71.26) -- (329.87,85.01) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (329.87,85.01) .. controls (329.04,84.61) and (329.84,81.2) .. (331.68,77.41) .. controls (333.51,73.61) and (335.67,70.86) .. (336.5,71.26) .. controls (337.34,71.67) and (336.53,75.07) .. (334.7,78.87) .. controls (332.87,82.66) and (330.71,85.41) .. (329.87,85.01) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (330.1,84.54) .. controls (329.43,84.21) and (330.26,81.09) .. (331.97,77.55) .. controls (333.68,74.01) and (335.6,71.41) .. (336.28,71.74) .. controls (336.95,72.06) and (336.11,75.19) .. (334.41,78.72) .. controls (332.7,82.26) and (330.77,84.86) .. (330.1,84.54) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (330.96,84.65) .. controls (330.19,84.28) and (330.9,81.22) .. (332.54,77.82) .. controls (334.18,74.42) and (336.13,71.97) .. (336.89,72.34) .. controls (337.66,72.7) and (336.95,75.76) .. (335.31,79.16) .. controls (333.67,82.56) and (331.72,85.02) .. (330.96,84.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (330.96,84.65) -- (336.89,72.34) -- (341.4,74.51) -- (335.46,86.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (335.46,86.82) .. controls (334.7,86.45) and (335.41,83.4) .. (337.05,80) .. controls (338.69,76.6) and (340.63,74.14) .. (341.4,74.51) .. controls (342.16,74.88) and (341.46,77.93) .. (339.82,81.33) .. controls (338.18,84.73) and (336.23,87.19) .. (335.46,86.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (335.66,86.4) .. controls (335.05,86.1) and (335.79,83.29) .. (337.32,80.13) .. controls (338.84,76.96) and (340.58,74.63) .. (341.2,74.93) .. controls (341.81,75.23) and (341.07,78.04) .. (339.55,81.2) .. controls (338.02,84.37) and (336.28,86.7) .. (335.66,86.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (335.93,86.2) .. controls (335.31,85.9) and (335.99,83.21) .. (337.45,80.19) .. controls (338.91,77.17) and (340.59,74.97) .. (341.21,75.27) .. controls (341.83,75.56) and (341.15,78.26) .. (339.7,81.28) .. controls (338.24,84.3) and (336.55,86.5) .. (335.93,86.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (335.93,86.2) -- (341.21,75.27) -- (344.86,77.03) -- (339.59,87.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (339.59,87.97) .. controls (338.97,87.67) and (339.65,84.98) .. (341.1,81.95) .. controls (342.56,78.93) and (344.24,76.73) .. (344.86,77.03) .. controls (345.49,77.33) and (344.81,80.02) .. (343.35,83.04) .. controls (341.89,86.06) and (340.21,88.27) .. (339.59,87.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (339.77,87.59) .. controls (339.27,87.35) and (339.97,84.87) .. (341.32,82.06) .. controls (342.68,79.25) and (344.18,77.16) .. (344.68,77.4) .. controls (345.18,77.64) and (344.49,80.12) .. (343.13,82.93) .. controls (341.77,85.75) and (340.27,87.83) .. (339.77,87.59) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (340.66,87.64) .. controls (339.89,87.26) and (340.3,84.82) .. (341.57,82.18) .. controls (342.85,79.54) and (344.5,77.7) .. (345.27,78.07) .. controls (346.04,78.44) and (345.64,80.89) .. (344.36,83.53) .. controls (343.09,86.17) and (341.43,88.01) .. (340.66,87.64) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (340.32,87.47) -- (344.93,77.91) -- (350.59,80.63) -- (345.97,90.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (345.97,90.2) .. controls (345.01,89.73) and (345.27,87.22) .. (346.54,84.58) .. controls (347.81,81.94) and (349.63,80.17) .. (350.59,80.63) .. controls (351.55,81.1) and (351.29,83.61) .. (350.02,86.25) .. controls (348.74,88.9) and (346.93,90.66) .. (345.97,90.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (346.13,89.87) .. controls (345.36,89.5) and (345.69,87.2) .. (346.88,84.74) .. controls (348.07,82.28) and (349.65,80.59) .. (350.43,80.96) .. controls (351.2,81.33) and (350.86,83.63) .. (349.68,86.09) .. controls (348.49,88.55) and (346.9,90.24) .. (346.13,89.87) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (346.81,89.82) .. controls (346.47,89.65) and (347.05,87.73) .. (348.11,85.52) .. controls (349.18,83.32) and (350.32,81.67) .. (350.67,81.83) .. controls (351.01,82) and (350.43,83.92) .. (349.37,86.13) .. controls (348.3,88.33) and (347.16,89.99) .. (346.81,89.82) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (346.66,89.74) -- (350.51,81.76) -- (353.06,82.99) -- (349.21,90.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (349.21,90.97) .. controls (348.77,90.76) and (349.29,88.81) .. (350.35,86.6) .. controls (351.41,84.4) and (352.63,82.78) .. (353.06,82.99) .. controls (353.49,83.19) and (352.98,85.15) .. (351.91,87.36) .. controls (350.85,89.56) and (349.64,91.18) .. (349.21,90.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (349.16,90.95) .. controls (348.5,90.63) and (348.83,88.59) .. (349.9,86.38) .. controls (350.96,84.18) and (352.36,82.65) .. (353.01,82.96) .. controls (353.67,83.28) and (353.35,85.33) .. (352.28,87.53) .. controls (351.22,89.74) and (349.82,91.27) .. (349.16,90.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (351.08,89.08) .. controls (350.65,88.87) and (350.68,87.93) .. (351.13,86.98) .. controls (351.59,86.03) and (352.31,85.43) .. (352.74,85.64) .. controls (353.17,85.84) and (353.15,86.78) .. (352.69,87.73) .. controls (352.24,88.68) and (351.52,89.28) .. (351.08,89.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (336.86,81.05) -- (337.75,79.2) -- (345.95,83.15) -- (345.06,85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (343.43,78.74) -- (347.49,80.84) -- (346.68,81.75) -- (342.62,79.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (340.13,84.7) -- (344.19,86.81) -- (344.06,88.07) -- (340,85.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (330.87,81.94) -- (335.01,83.87) -- (334.75,85.05) -- (330.61,83.12) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (325.02,79.69) -- (329.51,81.78) -- (329.23,83.04) -- (324.74,80.94) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (335.82,84.18) -- (339.27,85.79) -- (339.04,86.82) -- (335.59,85.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (339.84,86.29) -- (344.85,88.79) -- (344.91,89.44) -- (339.9,86.94) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (346.18,89.09) -- (348.46,90.22) -- (348.43,89.88) -- (346.15,88.74) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (354.56,101.71) .. controls (350.7,99.85) and (349.87,93.59) .. (352.69,87.73) .. controls (355.52,81.87) and (360.94,78.63) .. (364.79,80.49) .. controls (368.65,82.35) and (369.48,88.61) .. (366.65,94.47) .. controls (363.83,100.33) and (358.41,103.57) .. (354.56,101.71) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (355.89,102.35) .. controls (352.77,100.85) and (352.54,94.88) .. (355.36,89.02) .. controls (358.19,83.16) and (363.01,79.63) .. (366.13,81.13) .. controls (369.24,82.64) and (369.48,88.61) .. (366.65,94.47) .. controls (363.83,100.33) and (359.01,103.86) .. (355.89,102.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (355.58,89.94) -- (356.08,88.91) -- (359.53,90.57) -- (359.04,91.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (353.98,95.66) -- (354.04,95.2) -- (371.92,97.34) -- (371.86,97.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (364.79,81.36) -- (365.19,81.16) -- (372.9,97.04) -- (372.5,97.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (361.96,100.24) -- (361.86,99.83) -- (371.76,97.39) -- (371.86,97.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (369.02,96.33) .. controls (368.82,96.24) and (368.74,96.01) .. (368.84,95.81) -- (369.34,94.77) .. controls (369.43,94.57) and (369.67,94.49) .. (369.86,94.59) -- (375.36,97.24) .. controls (375.55,97.33) and (375.63,97.56) .. (375.54,97.76) -- (375.03,98.8) .. controls (374.94,98.99) and (374.71,99.08) .. (374.51,98.98) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (340.66,76.79) -- (344.82,53.61) -- (345.88,53.8) -- (341.72,76.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (331.85,62.82) -- (355.23,59.71) -- (353.2,72.86) -- (329.82,75.97) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (330.75,72.04) -- (353.41,68.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (331.31,67.77) -- (353.97,64.63) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (341.39,74.33) -- (343.67,61.35) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (335.82,75.04) -- (338.1,62.06) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (347.66,73.48) -- (349.94,60.5) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (334.28,47) -- (357.66,43.88) -- (355.63,57.04) -- (332.25,60.15) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (333.17,56.22) -- (355.83,53.08) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (333.74,51.95) -- (356.39,48.81) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (343.81,58.51) -- (346.09,45.53) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (338.25,59.22) -- (340.52,46.24) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (350.09,57.66) -- (352.36,44.68) ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Giả sử Trái Đất là một hình cầu có bán kính thực tế là $6400$ km. Trong không gian với hệ trục tọa độ $Oxyz$ (đơn vị trên các trục tương ứng với tỉ lệ mô hình), bề mặt Trái Đất có phương trình $x^2 + y^2 + z^2 = 64$, đường xích đạo nằm trên mặt phẳng $(Oxy)$. Một vệ tinh viễn thông được phóng từ bệ phóng tại điểm $A(4; 4\sqrt{2}; 4)$ nằm trên bề mặt Trái Đất. Vệ tinh bay theo phương tiếp tuyến với đường tròn vĩ tuyến tại điểm $A$ (trong mặt phẳng song song với $Oxy$) với quỹ đạo thẳng và vận tốc không đổi là $%s$ km/s. Sau đúng $%s$ phút bay thì vệ tinh đạt đến độ cao bao nhiêu kilomet so với bề mặt Trái Đất?}{%s}''' % (v, t, hinhve))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai = ('Trên mô hình, bán kính trái đất $R_{mohinh} = \\sqrt{64} = 8$ đơn vị và trong thực tế thì $R_{thucte} = 6400$ km.\\\\\n'
                    'Suy ra tỷ lệ quy đổi là: $k = \\frac{R_{thucte}}{R_{mohinh}} = \\frac{6400}{8} = 800$ (km/đơn vị), nghĩa là $1$ đơn vị độ dài trong hệ trục tọa độ tương ứng với $800$ km ngoài thực tế.\\\\\n'
                    'Quãng đường vệ tinh bay được là: $S = v \\cdot t = %s \\cdot %s = %s$ (km).\\\\\n'
                    'Gọi $O$ là tâm trái đất và $A$ là điểm phóng vệ tinh.\\\\\n'
                    'Do $A$ nằm trên bề mặt trái đất nên độ dài đoạn $OA$ chính là bán kính thực tế $OA = 6400$ km.\\\\\n'
                    'Gọi $B$ là vị trí của vệ tinh sau $%s$ phút bay thì đoạn đường $AB$ chính là quãng đường bay nên suy ra $AB = S = %s$ (km).\\\\\n'
                    'Theo giả thiết, vệ tinh bay theo phương tiếp tuyến với đường tròn vĩ tuyến tại điểm $A$ (trong mặt phẳng song song với $Oxy$) nên $AB \\perp Oz$.\\\\\n'
                    'Mặt khác, vectơ $\\overrightarrow{AB}$ vuông góc với mặt phẳng chứa trục $Oz$ và điểm $A$ nên $AB \\perp OA$.\\\\\n'
                    'Vậy tam giác $OAB$ là tam giác vuông tại $A$.\\\\\n'
                    'Khi đó độ cao của vệ tinh chính là hiệu số giữa khoảng cách từ tâm trái đất đến vị tinh.\\\\\n'
                    'Áp dụng định lý Pytago trong $\\triangle OAB$: $OB^2 = OA^2 + AB^2 \\Rightarrow OB = \\sqrt{6400^2 + %s^2} = %s$ (km).\\\\\n'
                    'Vậy sau $%s$ phút bay, vệ tinh đạt đến độ cao $h = %s - 6400 = %s$ (km) so với mặt đất.' 
                    % (v, t*60, S, t, S, S, OB, t, OB, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

