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


def bt_dang44_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tham số
            k = 2
            f_expr = "\\dfrac{1}{2}(1 - \\cos \\alpha)"

            # Nội dung câu hỏi
            noidungcauhoi = (
                """Khi Mặt Trăng quay quanh Trái Đất, mặt đối diện với Trái Đất thường chỉ được Mặt Trời chiếu sáng một phần. Các pha của Mặt Trăng mô tả mức độ phần bề mặt của nó được Mặt Trời chiếu sáng. Khi các góc giữa Mặt Trời, Trái Đất và Mặt Trăng là $\\alpha$ ($0^\\circ \\le \\alpha \\le 360^\\circ$) thì tỉ lệ $F$ của phần Mặt Trăng được chiếu sáng cho bởi công thức $F = %s$.
            \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (38.9,280.9) -- (486.9,280.9) -- (486.9,87.4) -- (38.9,87.4) -- cycle ;
            		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.36 ] (64.9,188.12) .. controls (64.9,150.97) and (95.02,120.85) .. (132.18,120.85) .. controls (169.33,120.85) and (199.45,150.97) .. (199.45,188.12) .. controls (199.45,225.28) and (169.33,255.4) .. (132.18,255.4) .. controls (95.02,255.4) and (64.9,225.28) .. (64.9,188.12) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.3 ] (396.6,184.4) .. controls (396.6,173.35) and (405.55,164.4) .. (416.6,164.4) .. controls (427.65,164.4) and (436.6,173.35) .. (436.6,184.4) .. controls (436.6,195.45) and (427.65,204.4) .. (416.6,204.4) .. controls (405.55,204.4) and (396.6,195.45) .. (396.6,184.4) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.6 ] (398.71,184.4) .. controls (398.71,174.52) and (406.72,166.51) .. (416.6,166.51) .. controls (426.48,166.51) and (434.49,174.52) .. (434.49,184.4) .. controls (434.49,194.28) and (426.48,202.29) .. (416.6,202.29) .. controls (406.72,202.29) and (398.71,194.28) .. (398.71,184.4) -- cycle ;
            		\\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (401.01,184.4) .. controls (401.01,175.79) and (407.99,168.81) .. (416.6,168.81) .. controls (425.21,168.81) and (432.19,175.79) .. (432.19,184.4) .. controls (432.19,193.01) and (425.21,199.99) .. (416.6,199.99) .. controls (407.99,199.99) and (401.01,193.01) .. (401.01,184.4) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (406.48,179.39) .. controls (406.94,179.15) and (408.98,178.91) .. (408.53,179.39) .. controls (408.07,179.88) and (408.07,180.13) .. (408.53,180.86) .. controls (408.98,181.59) and (406.94,181.59) .. (406.48,180.86) .. controls (406.03,180.13) and (406.03,179.64) .. (406.48,179.39) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.73 ] (414.34,180.33) .. controls (414.79,180.11) and (416.84,179.88) .. (416.38,180.33) .. controls (415.93,180.78) and (415.93,181) .. (416.38,181.67) .. controls (416.84,182.35) and (414.79,182.35) .. (414.34,181.67) .. controls (413.88,181) and (413.88,180.55) .. (414.34,180.33) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (409.76,173.5) .. controls (410.25,173.22) and (412.46,172.93) .. (411.97,173.5) .. controls (411.48,174.07) and (411.48,174.36) .. (411.97,175.21) .. controls (412.46,176.07) and (410.25,176.07) .. (409.76,175.21) .. controls (409.27,174.36) and (409.27,173.79) .. (409.76,173.5) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (415.18,175.95) .. controls (415.53,175.7) and (417.12,175.45) .. (416.77,175.95) .. controls (416.41,176.45) and (416.41,176.7) .. (416.77,177.44) .. controls (417.12,178.19) and (415.53,178.19) .. (415.18,177.44) .. controls (414.83,176.7) and (414.83,176.2) .. (415.18,175.95) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (419.74,180.17) .. controls (420.31,179.92) and (422.86,179.67) .. (422.29,180.17) .. controls (421.72,180.66) and (421.72,180.91) .. (422.29,181.66) .. controls (422.86,182.4) and (420.31,182.4) .. (419.74,181.66) .. controls (419.18,180.91) and (419.18,180.41) .. (419.74,180.17) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (406.12,184.54) .. controls (406.61,184.32) and (408.82,184.1) .. (408.33,184.54) .. controls (407.84,184.99) and (407.84,185.22) .. (408.33,185.89) .. controls (408.82,186.56) and (406.61,186.56) .. (406.12,185.89) .. controls (405.63,185.22) and (405.63,184.77) .. (406.12,184.54) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.73 ] (410.83,178.8) .. controls (411.25,178.57) and (413.16,178.35) .. (412.73,178.8) .. controls (412.31,179.26) and (412.31,179.49) .. (412.73,180.17) .. controls (413.16,180.85) and (411.25,180.85) .. (410.83,180.17) .. controls (410.4,179.49) and (410.4,179.03) .. (410.83,178.8) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.73 ] (411.32,183.42) .. controls (411.88,183.17) and (414.43,182.93) .. (413.86,183.42) .. controls (413.3,183.92) and (413.3,184.17) .. (413.86,184.91) .. controls (414.43,185.66) and (411.88,185.66) .. (411.32,184.91) .. controls (410.75,184.17) and (410.75,183.67) .. (411.32,183.42) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (416.6,182.91) .. controls (417.17,182.66) and (419.71,182.41) .. (419.15,182.91) .. controls (418.58,183.41) and (418.58,183.65) .. (419.15,184.4) .. controls (419.71,185.15) and (417.17,185.15) .. (416.6,184.4) .. controls (416.03,183.65) and (416.03,183.16) .. (416.6,182.91) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.41 ] (414.57,186.87) .. controls (415.14,186.62) and (417.68,186.37) .. (417.12,186.87) .. controls (416.55,187.37) and (416.55,187.62) .. (417.12,188.36) .. controls (417.68,189.11) and (415.14,189.11) .. (414.57,188.36) .. controls (414.01,187.62) and (414.01,187.12) .. (414.57,186.87) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (409.27,187.37) .. controls (409.66,187.19) and (411.42,187) .. (411.03,187.37) .. controls (410.64,187.74) and (410.64,187.92) .. (411.03,188.47) .. controls (411.42,189.02) and (409.66,189.02) .. (409.27,188.47) .. controls (408.88,187.92) and (408.88,187.55) .. (409.27,187.37) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (415.8,177.92) .. controls (415.8,177.26) and (416.33,176.73) .. (416.99,176.73) .. controls (417.65,176.73) and (418.18,177.26) .. (418.18,177.92) .. controls (418.18,178.58) and (417.65,179.11) .. (416.99,179.11) .. controls (416.33,179.11) and (415.8,178.58) .. (415.8,177.92) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (423.46,185.58) .. controls (423.46,184.92) and (423.99,184.39) .. (424.65,184.39) .. controls (425.31,184.39) and (425.84,184.92) .. (425.84,185.58) .. controls (425.84,186.24) and (425.31,186.78) .. (424.65,186.78) .. controls (423.99,186.78) and (423.46,186.24) .. (423.46,185.58) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (415.93,186.87) .. controls (415.93,186.21) and (416.46,185.68) .. (417.12,185.68) .. controls (417.78,185.68) and (418.31,186.21) .. (418.31,186.87) .. controls (418.31,187.53) and (417.78,188.06) .. (417.12,188.06) .. controls (416.46,188.06) and (415.93,187.53) .. (415.93,186.87) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (408.33,184.54) .. controls (408.33,183.89) and (408.86,183.35) .. (409.52,183.35) .. controls (410.18,183.35) and (410.72,183.89) .. (410.72,184.54) .. controls (410.72,185.2) and (410.18,185.74) .. (409.52,185.74) .. controls (408.86,185.74) and (408.33,185.2) .. (408.33,184.54) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (411.03,188.47) .. controls (411.03,187.81) and (411.56,187.28) .. (412.22,187.28) .. controls (412.88,187.28) and (413.41,187.81) .. (413.41,188.47) .. controls (413.41,189.13) and (412.88,189.66) .. (412.22,189.66) .. controls (411.56,189.66) and (411.03,189.13) .. (411.03,188.47) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (419.65,189.04) .. controls (419.65,188.39) and (420.18,187.85) .. (420.84,187.85) .. controls (421.5,187.85) and (422.03,188.39) .. (422.03,189.04) .. controls (422.03,189.7) and (421.5,190.24) .. (420.84,190.24) .. controls (420.18,190.24) and (419.65,189.7) .. (419.65,189.04) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (415.43,193.26) .. controls (415.43,192.6) and (415.97,192.07) .. (416.63,192.07) .. controls (417.28,192.07) and (417.82,192.6) .. (417.82,193.26) .. controls (417.82,193.92) and (417.28,194.45) .. (416.63,194.45) .. controls (415.97,194.45) and (415.43,193.92) .. (415.43,193.26) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (424.24,177.55) .. controls (424.24,176.89) and (424.78,176.36) .. (425.44,176.36) .. controls (426.1,176.36) and (426.63,176.89) .. (426.63,177.55) .. controls (426.63,178.21) and (426.1,178.74) .. (425.44,178.74) .. controls (424.78,178.74) and (424.24,178.21) .. (424.24,177.55) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (419.65,174.29) .. controls (419.65,173.64) and (420.18,173.1) .. (420.84,173.1) .. controls (421.5,173.1) and (422.03,173.64) .. (422.03,174.29) .. controls (422.03,174.95) and (421.5,175.49) .. (420.84,175.49) .. controls (420.18,175.49) and (419.65,174.95) .. (419.65,174.29) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 10; green, 107; blue, 220 }  ,fill opacity=1 ] (100.7,188.12) .. controls (100.7,170.74) and (114.79,156.65) .. (132.18,156.65) .. controls (149.56,156.65) and (163.65,170.74) .. (163.65,188.12) .. controls (163.65,205.51) and (149.56,219.6) .. (132.18,219.6) .. controls (114.79,219.6) and (100.7,205.51) .. (100.7,188.12) -- cycle ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (119.99,175.71) .. controls (119.99,175.71) and (119.99,175.71) .. (119.99,175.71) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (113.34,169.8) .. controls (112.6,171.52) and (111.86,173.25) .. (111.12,174.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (111.73,175.96) .. controls (115.2,172.59) and (116.17,169.95) .. (116.17,173.99) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (116.66,175.09) .. controls (115.88,175.75) and (113.72,176.47) .. (114.44,177.19) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (116.17,177.19) .. controls (116.17,177.19) and (116.17,177.19) .. (116.17,177.19) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (118.26,176.82) .. controls (118.75,175.75) and (120.14,174.72) .. (119.74,173.62) .. controls (119.13,171.95) and (117.21,171.12) .. (115.8,170.05) .. controls (115.4,169.74) and (116.37,170.87) .. (116.66,171.28) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (113.7,167.83) .. controls (114.11,167.58) and (114.53,167.34) .. (114.94,167.09) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (113.95,167.09) .. controls (113.5,166.93) and (113.05,166.76) .. (112.6,166.6) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (111.98,168.69) .. controls (111.65,168.36) and (111.32,168.03) .. (111,167.71) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (111.12,169.8) .. controls (110.67,169.96) and (110.22,170.13) .. (109.76,170.29) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (110.01,171.77) .. controls (109.68,171.93) and (109.35,172.1) .. (109.02,172.26) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (109.27,173.74) .. controls (108.78,173.9) and (108.29,174.07) .. (107.79,174.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (108.16,174.97) .. controls (107.59,175.3) and (107.01,175.63) .. (106.44,175.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (106.93,176.2) .. controls (106.89,176.57) and (106.85,176.94) .. (106.81,177.31) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (109.27,176.2) .. controls (109.27,176.9) and (109.27,177.6) .. (109.27,178.3) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (110.75,177.56) .. controls (110.95,177.76) and (111.16,177.97) .. (111.36,178.17) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (112.47,178.05) .. controls (112.64,178.05) and (112.8,178.05) .. (112.97,178.05) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (108.16,179.65) .. controls (108.45,179.77) and (108.74,179.9) .. (109.02,180.02) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (127.5,200.09) .. controls (126.43,198.45) and (125.36,196.81) .. (124.3,195.17) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (124.3,194.8) .. controls (123.56,193.44) and (122.82,192.09) .. (122.08,190.73) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (125.53,201.08) .. controls (123.84,198.49) and (122.16,195.91) .. (120.48,193.32) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (121.59,199.72) .. controls (120.93,198.62) and (120.27,197.51) .. (119.62,196.4) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (130.21,199.6) .. controls (128.48,196.73) and (126.76,193.85) .. (125.03,190.98) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (132.18,202.31) .. controls (132.71,200.67) and (133.24,199.03) .. (133.78,197.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.41,198.86) .. controls (132.05,196.89) and (130.7,194.92) .. (129.34,192.95) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.41,197.88) .. controls (133.98,198.04) and (134.56,198.2) .. (135.13,198.37) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (134.39,199.85) .. controls (134.39,200.18) and (134.39,200.5) .. (134.39,200.83) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.78,202.31) .. controls (133.78,202.56) and (133.78,202.8) .. (133.78,203.05) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (131.68,203.3) .. controls (131.44,203.66) and (131.19,204.03) .. (130.95,204.4) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (129.96,204.4) .. controls (130.04,204.98) and (130.12,205.55) .. (130.21,206.13) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (128.85,206.74) .. controls (129.14,206.83) and (129.43,206.91) .. (129.71,206.99) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (127.25,207.48) .. controls (127.46,207.89) and (127.66,208.3) .. (127.87,208.71) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (127.37,208.71) .. controls (127.25,209.17) and (127.13,209.62) .. (127,210.07) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (125.53,209.82) .. controls (125.53,210.23) and (125.53,210.64) .. (125.53,211.05) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (125.16,209.08) .. controls (125.16,206.66) and (125.16,204.24) .. (125.16,201.82) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (126.64,205.02) .. controls (127.44,203.66) and (128.09,201.99) .. (129.47,201.2) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (125.77,202.93) .. controls (125.16,202.43) and (124.54,201.94) .. (123.93,201.45) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (152.62,181.13) .. controls (150.46,183.28) and (148.32,185.45) .. (146.09,187.53) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (146.22,186.3) .. controls (145.89,185.44) and (145.43,184.46) .. (145.72,183.59) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (146.22,182.73) .. controls (146.95,181.99) and (147.69,181.25) .. (148.43,180.51) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (148.8,180.14) .. controls (149.83,179.77) and (150.85,179.4) .. (151.88,179.03) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (152.62,179.9) .. controls (153.28,180.35) and (153.93,180.8) .. (154.59,181.25) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (156.07,182.24) .. controls (156.77,182.2) and (157.46,182.15) .. (158.16,182.11) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (158.65,182.11) .. controls (159.27,181.79) and (159.89,181.46) .. (160.5,181.13) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (160.75,181.25) .. controls (160.71,183.18) and (160.67,185.11) .. (160.62,187.04) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (161.49,184.82) .. controls (161.12,188.23) and (160.75,191.64) .. (160.38,195.04) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (159.15,186.92) .. controls (158.2,185.81) and (157.62,184.24) .. (156.31,183.59) .. controls (155.1,182.99) and (152.42,182.12) .. (152.25,183.47) .. controls (152.13,184.4) and (157.02,188.6) .. (158.16,189.63) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (156.07,187.04) .. controls (155.62,188.02) and (155.16,189.01) .. (154.71,190) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (153.85,189.38) .. controls (152.77,188.09) and (151.57,186.84) .. (150.16,185.93) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (149.66,186.42) .. controls (149.87,187.41) and (150.07,188.39) .. (150.28,189.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (147.82,188.27) .. controls (147.98,188.97) and (148.15,189.67) .. (148.31,190.36) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (157.18,190) .. controls (157.09,191.14) and (157.01,192.29) .. (156.93,193.44) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (159.15,193.57) .. controls (158.86,194.02) and (158.57,194.47) .. (158.28,194.92) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (157.3,189.63) .. controls (157.75,190.16) and (158.2,190.69) .. (158.65,191.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (160.25,196.65) .. controls (160.09,197.26) and (159.93,197.88) .. (159.76,198.49) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (159.15,197.14) .. controls (159.11,197.34) and (159.06,197.55) .. (159.02,197.75) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (159.02,197.88) .. controls (158.69,199.07) and (158.37,200.26) .. (158.04,201.45) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (154.47,171.15) .. controls (154.67,171.03) and (154.88,170.91) .. (155.08,170.78) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (155.45,171.4) .. controls (155.49,171.44) and (155.53,171.48) .. (155.57,171.52) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (153.11,171.28) .. controls (152.41,171.28) and (151.72,171.28) .. (151.02,171.28) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=5.25] [line join = round][line cap = round] (132.92,162.04) .. controls (132.71,161.92) and (132.51,161.79) .. (132.3,161.67) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (115.18,166.1) .. controls (115.8,165.98) and (116.41,165.86) .. (117.03,165.73) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (116.41,166.84) .. controls (116.62,166.68) and (116.82,166.51) .. (117.03,166.35) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.46,165.24) .. controls (113.62,165.24) and (113.79,165.24) .. (113.95,165.24) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (114.2,165.49) .. controls (114.16,165.28) and (114.11,165.08) .. (114.07,164.87) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.15,165.86) .. controls (118.06,165.49) and (118.96,165.12) .. (119.86,164.75) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (118.26,166.35) .. controls (118.67,166.02) and (119.08,165.69) .. (119.49,165.37) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.89,166.1) .. controls (117.4,166.68) and (116.91,167.25) .. (116.41,167.83) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (104.71,177.19) .. controls (104.92,178.5) and (105.13,179.81) .. (105.33,181.13) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.7,179.65) .. controls (114.53,179.49) and (115.35,179.32) .. (116.17,179.16) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.17,179.53) .. controls (116.41,179.61) and (116.66,179.69) .. (116.91,179.77) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.89,178.67) .. controls (117.69,178.99) and (117.48,179.32) .. (117.28,179.65) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.28,179.4) .. controls (117.48,180.18) and (117.69,180.96) .. (117.89,181.74) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (110.75,180.14) .. controls (110.58,181.17) and (110.42,182.2) .. (110.26,183.22) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.9,181.37) .. controls (109.31,182.24) and (109.72,183.1) .. (110.13,183.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (109.02,181.74) .. controls (109.27,182.61) and (109.52,183.47) .. (109.76,184.33) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.16,181.62) .. controls (108.41,182.28) and (108.66,182.93) .. (108.9,183.59) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (107.92,181.74) .. controls (108.33,182.61) and (108.74,183.47) .. (109.15,184.33) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (111.49,179.4) .. controls (111.32,179.9) and (111.16,180.39) .. (111,180.88) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (109.52,181.62) .. controls (109.6,181.95) and (109.68,182.28) .. (109.76,182.61) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (107.79,182.85) .. controls (108.78,183.76) and (109.76,184.66) .. (110.75,185.56) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.41,184.21) .. controls (109.19,184.62) and (109.97,185.03) .. (110.75,185.44) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (110.5,183.59) .. controls (111.36,184.49) and (112.23,185.4) .. (113.09,186.3) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (111.24,185.19) .. controls (111.73,185.64) and (112.23,186.1) .. (112.72,186.55) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (110.75,184.33) .. controls (111.57,184.9) and (112.22,186.16) .. (113.21,186.05) .. controls (114,185.97) and (113.95,184.66) .. (114.32,183.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.46,185.32) .. controls (113.54,185.07) and (113.62,184.82) .. (113.7,184.58) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.46,186.55) .. controls (114.11,187.04) and (114.77,187.53) .. (115.43,188.02) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (114.07,187.04) .. controls (114.69,187.08) and (115.31,187.12) .. (115.92,187.16) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (115.92,187.78) .. controls (115.92,188.27) and (115.92,188.76) .. (115.92,189.26) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.17,189.13) .. controls (116.66,189.3) and (117.15,189.46) .. (117.65,189.63) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (118.14,190) .. controls (118.92,190.61) and (119.7,191.23) .. (120.48,191.84) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (119,190.98) .. controls (119,191.31) and (119,191.64) .. (119,191.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (119.37,190.49) .. controls (120.07,189.95) and (120.77,189.42) .. (121.46,188.89) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.69,189.26) .. controls (123.39,189.13) and (124.09,189.01) .. (124.79,188.89) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127,191.35) .. controls (127.5,191.35) and (127.99,191.35) .. (128.48,191.35) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.89,196.4) .. controls (135.8,197.31) and (137.5,198.61) .. (136.86,199.72) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.36,196.52) .. controls (136.86,197.06) and (137.35,197.59) .. (137.84,198.12) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.61,197.88) .. controls (136.36,197.38) and (136.12,196.89) .. (135.87,196.4) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.87,202.31) .. controls (135.5,202.84) and (135.13,203.38) .. (134.76,203.91) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.05,206.74) .. controls (131.97,207.15) and (131.89,207.56) .. (131.81,207.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.76,211.55) .. controls (127.17,211.87) and (127.58,212.2) .. (127.99,212.53) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.36,210.07) .. controls (128.85,210.23) and (129.34,210.4) .. (129.84,210.56) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.1,210.07) .. controls (129.55,209.53) and (130,209) .. (130.45,208.47) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.8,211.3) .. controls (124.42,212.41) and (125.03,213.52) .. (125.65,214.62) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.65,213.02) .. controls (125.77,213.39) and (125.9,213.76) .. (126.02,214.13) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.53,214.62) .. controls (126.14,215.4) and (126.76,216.18) .. (127.37,216.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (119.49,164.87) .. controls (120.07,164.71) and (120.64,164.54) .. (121.22,164.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.09,164.87) .. controls (120.93,164.3) and (120.76,163.72) .. (120.6,163.15) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.6,162.9) .. controls (121.96,162.86) and (123.31,162.82) .. (124.66,162.78) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.56,162.9) .. controls (123.35,163.31) and (123.15,163.72) .. (122.94,164.13) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.05,162.78) .. controls (124.91,163.27) and (125.77,163.76) .. (126.64,164.26) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.16,163.76) .. controls (125.32,164.46) and (125.49,165.16) .. (125.65,165.86) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.53,164.63) .. controls (125.49,165.04) and (125.44,165.45) .. (125.4,165.86) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.16,164.87) .. controls (124.79,165.16) and (124.42,165.45) .. (124.05,165.73) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.42,165.37) .. controls (124.83,165.57) and (125.24,165.78) .. (125.65,165.98) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.04,163.4) .. controls (116.37,163.6) and (116.7,163.81) .. (117.03,164.01) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.15,164.01) .. controls (117.77,163.76) and (118.38,163.52) .. (119,163.27) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.65,163.4) .. controls (117.52,163.11) and (117.4,162.82) .. (117.28,162.53) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.03,162.9) .. controls (116.91,162.98) and (116.78,163.07) .. (116.66,163.15) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (119.37,162.04) .. controls (119.62,161.96) and (119.86,161.88) .. (120.11,161.79) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.59,161.67) .. controls (121.79,161.51) and (122,161.34) .. (122.2,161.18) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.68,161.67) .. controls (124.21,161.47) and (124.75,161.26) .. (125.28,161.06) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.91,160.93) .. controls (124.66,160.77) and (124.42,160.6) .. (124.17,160.44) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.28,160.93) .. controls (125.9,160.56) and (126.51,160.19) .. (127.13,159.82) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.14,160.44) .. controls (127.13,160.23) and (128.11,160.03) .. (129.1,159.82) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127,159.7) .. controls (126.76,159.7) and (126.51,159.7) .. (126.27,159.7) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (118.01,169.31) .. controls (118.63,169.72) and (119.25,170.13) .. (119.86,170.54) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.09,164.38) .. controls (114.2,164.67) and (115.31,164.95) .. (116.41,165.24) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.66,165.24) .. controls (117.6,164.95) and (118.55,164.67) .. (119.49,164.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.22,172.88) .. controls (122.53,171.29) and (123.49,169.09) .. (125.4,168.32) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.17,168.07) .. controls (124.01,167.66) and (123.84,167.25) .. (123.68,166.84) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.56,166.6) .. controls (123.19,167.5) and (122.82,168.4) .. (122.45,169.31) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.2,168.44) .. controls (122.2,168.98) and (122.2,169.51) .. (122.2,170.05) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.2,170.05) .. controls (122.2,170.13) and (122.2,170.21) .. (122.2,170.29) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.32,169.18) .. controls (121.75,169.88) and (121.18,170.58) .. (120.6,171.28) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.09,172.02) .. controls (121.92,170.52) and (124.64,168.67) .. (123.43,167.46) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.94,167.34) .. controls (122.74,167.58) and (122.53,167.83) .. (122.32,168.07) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.96,169.8) .. controls (121.79,170.13) and (121.63,170.46) .. (121.46,170.78) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.03,168.69) .. controls (125.59,168.34) and (126.66,168.26) .. (127,168.81) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.88,168.81) .. controls (127.37,169.35) and (127.87,169.88) .. (128.36,170.41) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.48,171.03) .. controls (128.32,171.44) and (128.15,171.85) .. (127.99,172.26) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.36,171.28) .. controls (128.39,171.61) and (128.15,172.31) .. (127.87,172.14) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.62,172.02) .. controls (127.74,171.44) and (127.87,170.87) .. (127.99,170.29) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.25,170.29) .. controls (126.06,170.54) and (124.87,170.78) .. (123.68,171.03) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.05,170.29) .. controls (125.03,169.92) and (126.02,169.55) .. (127,169.18) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.27,169.31) .. controls (125.65,169.59) and (125.03,169.88) .. (124.42,170.17) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.66,169.55) .. controls (125.12,168.94) and (125.57,168.32) .. (126.02,167.71) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.31,171.15) .. controls (123.31,171.15) and (123.31,171.15) .. (123.31,171.15) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.8,171.03) .. controls (124.21,171.73) and (124.62,172.43) .. (125.03,173.12) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.05,172.02) .. controls (123.84,172.43) and (123.64,172.84) .. (123.43,173.25) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.43,171.4) .. controls (123.06,172.38) and (122.69,173.37) .. (122.32,174.36) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.57,171.89) .. controls (122.41,172.92) and (122.24,173.94) .. (122.08,174.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.93,173) .. controls (124.34,173.33) and (124.75,173.66) .. (125.16,173.99) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.16,173.62) .. controls (125.4,173.49) and (125.65,173.37) .. (125.9,173.25) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.25,161.42) .. controls (129.3,160.81) and (131.36,160.19) .. (133.41,159.58) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.41,159.58) .. controls (135.3,159.86) and (137.18,160.15) .. (139.07,160.44) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.9,159.95) .. controls (135.23,160.4) and (136.6,161.4) .. (137.96,161.06) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.89,160.81) .. controls (136.04,161.14) and (137.18,161.47) .. (138.33,161.79) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.39,160.44) .. controls (135.38,161.1) and (136.36,161.75) .. (137.35,162.41) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.01,160.81) .. controls (134.93,162) and (134.84,163.19) .. (134.76,164.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.89,163.89) .. controls (135.83,163.64) and (136.77,163.4) .. (137.72,163.15) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.36,162.9) .. controls (136.2,162.57) and (136.04,162.25) .. (135.87,161.92) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.75,162.9) .. controls (135.01,161.92) and (134.27,160.93) .. (133.53,159.95) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.21,161.06) .. controls (130.04,161.18) and (129.88,161.3) .. (129.71,161.42) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.59,161.79) .. controls (129.92,162.33) and (130.25,162.86) .. (130.58,163.4) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.33,162.04) .. controls (130.66,162.53) and (130.99,163.03) .. (131.31,163.52) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.97,161.42) .. controls (130,162.7) and (131.03,163.97) .. (132.05,165.24) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.7,163.89) .. controls (130.9,164.71) and (131.11,165.53) .. (131.31,166.35) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.05,163.64) .. controls (132.51,163.89) and (132.96,164.13) .. (133.41,164.38) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.39,162.9) .. controls (134.31,163.48) and (134.23,164.05) .. (134.15,164.63) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.27,164.38) .. controls (133.53,165.08) and (132.79,165.78) .. (132.05,166.47) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.41,163.76) .. controls (133.04,164.3) and (132.67,164.83) .. (132.3,165.37) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.58,163.89) .. controls (130.53,164.3) and (130.49,164.71) .. (130.45,165.12) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.05,163.64) .. controls (132.01,164.5) and (131.97,165.37) .. (131.93,166.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.45,164.38) .. controls (130.78,165.08) and (131.11,165.78) .. (131.44,166.47) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.33,165.37) .. controls (130.86,166.02) and (131.4,166.68) .. (131.93,167.34) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.29,171.03) .. controls (148.84,171.44) and (148.39,171.85) .. (147.94,172.26) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (148.43,172.63) .. controls (148.68,173.16) and (148.92,173.7) .. (149.17,174.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.05,172.26) .. controls (149.42,172.75) and (149.79,173.25) .. (150.16,173.74) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (151.51,173.37) .. controls (150.53,173.99) and (149.54,174.6) .. (148.56,175.22) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.17,173.74) .. controls (148.68,174.07) and (148.19,174.4) .. (147.69,174.72) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.94,174.23) .. controls (147.24,174.19) and (146.54,174.15) .. (145.85,174.11) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (145.85,174.36) .. controls (146.13,175.09) and (146.42,175.83) .. (146.71,176.57) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.2,176.7) .. controls (147.86,176.2) and (148.51,175.71) .. (149.17,175.22) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (148.19,176.2) .. controls (147.98,175.96) and (147.78,175.71) .. (147.57,175.46) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.08,175.46) .. controls (147.41,175.22) and (148.06,175.01) .. (148.31,175.34) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.82,175.59) .. controls (148.31,175.14) and (148.8,174.68) .. (149.29,174.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (153.11,169.06) .. controls (153.4,168.69) and (153.69,168.32) .. (153.97,167.95) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (153.97,167.83) .. controls (154.02,167.58) and (154.06,167.34) .. (154.1,167.09) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (154.71,167.34) .. controls (155.12,167.99) and (155.53,168.65) .. (155.94,169.31) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (154.96,168.81) .. controls (155.16,169.18) and (155.37,169.55) .. (155.57,169.92) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (156.07,168.69) .. controls (156.97,170.21) and (157.87,171.73) .. (158.78,173.25) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (156.93,171.03) .. controls (157.79,172.34) and (158.65,173.66) .. (159.52,174.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (158.65,172.75) .. controls (159.19,173.82) and (159.72,174.89) .. (160.25,175.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (157.79,173.62) .. controls (158.2,174.4) and (158.61,175.18) .. (159.02,175.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (157.42,172.38) .. controls (157.34,173.16) and (157.26,173.94) .. (157.18,174.72) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (155.57,172.75) .. controls (156.73,174.56) and (156.99,175.09) .. (156.56,174.23) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (152.99,173.12) .. controls (153.56,173.94) and (154.14,174.77) .. (154.71,175.59) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (152.99,173.74) .. controls (153.11,174.03) and (153.24,174.31) .. (153.36,174.6) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (152.74,173.49) .. controls (153.36,174.19) and (153.97,174.89) .. (154.59,175.59) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (153.6,174.97) .. controls (153.85,175.09) and (154.1,175.22) .. (154.34,175.34) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (153.97,174.72) .. controls (153.15,174.4) and (152.33,174.07) .. (151.51,173.74) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (157.42,180.02) .. controls (157.67,179.57) and (157.91,179.12) .. (158.16,178.67) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (158.04,180.39) .. controls (158.57,180.02) and (159.11,179.65) .. (159.64,179.28) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (158.53,178.79) .. controls (159.27,179.08) and (160.01,179.36) .. (160.75,179.65) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (159.76,179.28) .. controls (161.66,178.52) and (162.08,179.01) .. (161.49,178.42) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (161.98,179.77) .. controls (161.81,179.32) and (161.65,178.87) .. (161.49,178.42) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (160.75,176.57) .. controls (161.03,177.11) and (161.32,177.64) .. (161.61,178.17) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (156.56,202.19) .. controls (156.89,203.01) and (157.22,203.83) .. (157.55,204.65) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (160.43,199.87) .. controls (159.74,201.42) and (159.05,202.96) .. (158.35,204.5) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (157.67,203.66) .. controls (157.46,204.69) and (157.26,205.72) .. (157.05,206.74) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (157.42,205.02) .. controls (157.42,205.59) and (157.42,206.17) .. (157.42,206.74) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (152.99,165.24) .. controls (152.17,164.5) and (151.35,163.76) .. (150.53,163.03) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (150.4,162.78) .. controls (149.99,162.98) and (149.58,163.19) .. (149.17,163.4) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.05,163.76) .. controls (148.64,164.63) and (148.23,165.49) .. (147.82,166.35) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.82,166.35) .. controls (148.27,166.76) and (148.72,167.17) .. (149.17,167.58) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.17,167.58) .. controls (149.83,167.54) and (150.48,167.5) .. (151.14,167.46) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (151.14,167.34) .. controls (150.9,166.15) and (150.65,164.95) .. (150.4,163.76) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (150.16,163.89) .. controls (150.03,164.79) and (149.91,165.69) .. (149.79,166.6) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.66,164.38) .. controls (149.46,165.12) and (149.25,165.86) .. (149.05,166.6) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.17,166.6) .. controls (149.58,166.72) and (149.99,166.84) .. (150.4,166.97) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (151.39,164.75) .. controls (152.13,165.41) and (152.87,166.06) .. (153.6,166.72) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (150.16,166.1) .. controls (150.03,166.31) and (149.91,166.51) .. (149.79,166.72) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (148.68,166.23) .. controls (148.84,166.43) and (149.01,166.64) .. (149.17,166.84) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (151.14,167.95) .. controls (151.1,168.07) and (151.06,168.2) .. (151.02,168.32) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (145.23,167.71) .. controls (146.09,168.44) and (146.95,169.18) .. (147.82,169.92) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (145.72,168.2) .. controls (145.19,168.44) and (144.66,168.69) .. (144.12,168.94) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (144.12,169.18) .. controls (144.16,169.55) and (144.2,169.92) .. (144.25,170.29) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (144.49,170.29) .. controls (144.98,169.8) and (145.48,169.31) .. (145.97,168.81) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (146.22,169.18) .. controls (146.63,169.51) and (147.04,169.84) .. (147.45,170.17) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.45,170.29) .. controls (147.2,170.46) and (146.95,170.62) .. (146.71,170.78) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (118.75,183.96) .. controls (119.7,183.96) and (120.64,183.96) .. (121.59,183.96) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.6,184.21) .. controls (121.34,184.33) and (122.08,184.45) .. (122.82,184.58) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.6,184.21) .. controls (120.52,184.21) and (120.44,184.21) .. (120.35,184.21) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.54,184.7) .. controls (124.58,184.7) and (124.62,184.7) .. (124.66,184.7) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (118.38,184.95) .. controls (118.47,184.95) and (118.55,184.95) .. (118.63,184.95) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (116.66,172.75) .. controls (118.38,172.88) and (120.11,173) .. (121.83,173.12) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (125.03,169.92) .. controls (125.57,169.88) and (126.1,169.84) .. (126.64,169.8) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (116.04,177.19) .. controls (116.29,177.56) and (116.54,177.93) .. (116.78,178.3) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (151.14,173) .. controls (151.63,173.08) and (152.13,173.16) .. (152.62,173.25) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (148.06,174.97) .. controls (147.78,174.93) and (147.49,174.89) .. (147.2,174.85) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (149.42,165.37) .. controls (149.17,165.37) and (148.92,165.37) .. (148.68,165.37) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (149.42,165.49) .. controls (149.62,165.32) and (149.83,165.16) .. (150.03,165) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (156.44,171.77) .. controls (156.68,172.22) and (156.93,172.67) .. (157.18,173.12) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (161.61,187.29) .. controls (161.69,188.44) and (161.77,189.58) .. (161.86,190.73) ;
            		\\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (161.49,191.97) .. controls (161.45,192.87) and (161.4,193.77) .. (161.36,194.67) ;
            		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (111.6,187.11) .. controls (107.74,179.57) and (112.14,169.6) .. (121.44,164.84) .. controls (130.74,160.07) and (141.41,162.32) .. (145.27,169.85) .. controls (149.13,177.39) and (144.72,187.36) .. (135.42,192.13) .. controls (126.13,196.89) and (115.46,194.64) .. (111.6,187.11) -- cycle ;
            		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (104.23,196.81) .. controls (97.64,183.95) and (104.09,167.49) .. (118.64,160.03) .. controls (133.19,152.58) and (150.32,156.96) .. (156.91,169.82) .. controls (163.5,182.68) and (157.05,199.14) .. (142.5,206.6) .. controls (127.95,214.05) and (110.82,209.67) .. (104.23,196.81) -- cycle ;
            		\\draw  [line width=0.75]  (100.7,188.12) .. controls (100.7,170.74) and (114.79,156.65) .. (132.18,156.65) .. controls (149.56,156.65) and (163.65,170.74) .. (163.65,188.12) .. controls (163.65,205.51) and (149.56,219.6) .. (132.18,219.6) .. controls (114.79,219.6) and (100.7,205.51) .. (100.7,188.12) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 210; green, 205; blue, 205 }  ,fill opacity=1 ] (161.6,137.15) .. controls (161.6,130.66) and (166.86,125.4) .. (173.35,125.4) .. controls (179.84,125.4) and (185.1,130.66) .. (185.1,137.15) .. controls (185.1,143.64) and (179.84,148.9) .. (173.35,148.9) .. controls (166.86,148.9) and (161.6,143.64) .. (161.6,137.15) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (171.6,130.74) .. controls (172.06,130.51) and (172.56,130.93) .. (173.6,130.95) .. controls (175.34,130.98) and (176.95,130.05) .. (176.19,130.8) .. controls (174.98,132.01) and (172.6,131.31) .. (173.81,133.12) .. controls (174.5,134.16) and (174.43,134.33) .. (172.81,134.18) .. controls (171.6,134.07) and (171.27,135.2) .. (170.75,134.43) .. controls (170.24,133.66) and (171.02,132.76) .. (170.97,132.04) .. controls (170.91,131.04) and (170.91,131.09) .. (171.6,130.74) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (168.15,134.45) .. controls (167.98,134.18) and (168.39,133.96) .. (168.49,133.4) .. controls (168.65,132.47) and (167.96,131.48) .. (168.56,131.99) .. controls (169.52,132.79) and (168.73,133.99) .. (170.41,133.56) .. controls (171.37,133.32) and (171.51,133.38) .. (171.26,134.23) .. controls (171.06,134.87) and (172.03,135.19) .. (171.31,135.37) .. controls (170.6,135.55) and (169.87,135.02) .. (169.24,134.96) .. controls (168.36,134.87) and (168.4,134.87) .. (168.15,134.45) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (171.89,128.52) .. controls (172.3,128.6) and (172.28,129.17) .. (172.83,129.74) .. controls (173.76,130.69) and (175.29,130.88) .. (174.34,131.02) .. controls (172.84,131.24) and (172.03,129.46) .. (171.42,131.4) .. controls (171.07,132.51) and (170.92,132.6) .. (170.14,131.62) .. controls (169.55,130.89) and (168.58,131.53) .. (168.84,130.7) .. controls (169.1,129.88) and (170.15,129.65) .. (170.64,129.11) .. controls (171.3,128.37) and (171.27,128.4) .. (171.89,128.52) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (173.79,135.05) .. controls (174.68,134.6) and (178.69,134.15) .. (177.8,135.05) .. controls (176.91,135.94) and (176.91,136.38) .. (177.8,137.72) .. controls (178.69,139.06) and (174.68,139.06) .. (173.79,137.72) .. controls (172.9,136.38) and (172.9,135.49) .. (173.79,135.05) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (169.24,134.96) .. controls (169.35,135.95) and (168.42,139.87) .. (167.88,138.73) .. controls (167.34,137.59) and (166.92,137.44) .. (165.36,137.83) .. controls (163.81,138.21) and (165.16,134.44) .. (166.72,134.05) .. controls (168.28,133.67) and (169.12,133.97) .. (169.24,134.96) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (171.78,137.46) .. controls (172.67,137.02) and (176.68,136.57) .. (175.79,137.46) .. controls (174.89,138.35) and (174.89,138.8) .. (175.79,140.14) .. controls (176.68,141.47) and (172.67,141.47) .. (171.78,140.14) .. controls (170.88,138.8) and (170.88,137.91) .. (171.78,137.46) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (173.69,146.12) .. controls (172.57,146.12) and (163.57,142.51) .. (164.92,142.06) .. controls (166.26,141.62) and (166.48,141.17) .. (166.26,139.39) .. controls (166.04,137.6) and (170.06,139.62) .. (170.28,141.41) .. controls (170.5,143.2) and (174.8,146.12) .. (173.69,146.12) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (175.95,144.77) .. controls (175.41,144.77) and (171.07,143.03) .. (171.72,142.81) .. controls (172.36,142.6) and (172.47,142.38) .. (172.37,141.52) .. controls (172.26,140.66) and (174.2,141.63) .. (174.3,142.5) .. controls (174.41,143.36) and (176.49,144.77) .. (175.95,144.77) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (180.57,138.7) .. controls (180.63,139.33) and (179.01,144.6) .. (178.69,143.86) .. controls (178.38,143.12) and (178.12,143.02) .. (177.11,143.23) .. controls (176.11,143.43) and (177.07,141.06) .. (178.07,140.86) .. controls (179.07,140.65) and (180.52,138.07) .. (180.57,138.7) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (182.52,131.96) .. controls (181.83,131.12) and (173.53,126.13) .. (174.02,127.37) .. controls (174.52,128.61) and (174.32,129) .. (172.83,129.74) .. controls (171.34,130.47) and (175.36,132.49) .. (176.84,131.76) .. controls (178.33,131.02) and (183.22,132.81) .. (182.52,131.96) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (182.09,134.59) .. controls (181.66,134.07) and (176.54,130.99) .. (176.84,131.76) .. controls (177.15,132.52) and (177.03,132.76) .. (176.11,133.22) .. controls (175.19,133.67) and (177.67,134.92) .. (178.59,134.46) .. controls (179.5,134.01) and (182.52,135.11) .. (182.09,134.59) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.43 ] (162.73,135.29) .. controls (162.73,130.08) and (166.95,125.85) .. (172.17,125.85) .. controls (177.38,125.85) and (181.61,130.08) .. (181.61,135.29) .. controls (181.61,140.51) and (177.38,144.74) .. (172.17,144.74) .. controls (166.95,144.74) and (162.73,140.51) .. (162.73,135.29) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.43 ] (164.23,132.18) .. controls (164.23,129.32) and (166.55,127.01) .. (169.41,127.01) .. controls (172.26,127.01) and (174.58,129.32) .. (174.58,132.18) .. controls (174.58,135.04) and (172.26,137.35) .. (169.41,137.35) .. controls (166.55,137.35) and (164.23,135.04) .. (164.23,132.18) -- cycle ;
            		\\draw  [line width=6]  (96.4,188.12) .. controls (96.4,168.36) and (112.42,152.35) .. (132.18,152.35) .. controls (151.94,152.35) and (167.95,168.36) .. (167.95,188.12) .. controls (167.95,207.88) and (151.94,223.9) .. (132.18,223.9) .. controls (112.42,223.9) and (96.4,207.88) .. (96.4,188.12) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 157; green, 225; blue, 210 }  ,fill opacity=1 ] (392,121.2) .. controls (392,120.21) and (392.81,119.4) .. (393.8,119.4) .. controls (394.79,119.4) and (395.6,120.21) .. (395.6,121.2) .. controls (395.6,122.19) and (394.79,123) .. (393.8,123) .. controls (392.81,123) and (392,122.19) .. (392,121.2) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 205; blue, 205 }  ,fill opacity=1 ] (262.5,243.7) .. controls (262.5,242.98) and (263.08,242.4) .. (263.8,242.4) .. controls (264.52,242.4) and (265.1,242.98) .. (265.1,243.7) .. controls (265.1,244.42) and (264.52,245) .. (263.8,245) .. controls (263.08,245) and (262.5,244.42) .. (262.5,243.7) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 205; blue, 205 }  ,fill opacity=1 ] (286.5,179.7) .. controls (286.5,178.98) and (287.08,178.4) .. (287.8,178.4) .. controls (288.52,178.4) and (289.1,178.98) .. (289.1,179.7) .. controls (289.1,180.42) and (288.52,181) .. (287.8,181) .. controls (287.08,181) and (286.5,180.42) .. (286.5,179.7) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 205; blue, 205 }  ,fill opacity=1 ] (315,215.7) .. controls (315,214.98) and (315.58,214.4) .. (316.3,214.4) .. controls (317.02,214.4) and (317.6,214.98) .. (317.6,215.7) .. controls (317.6,216.42) and (317.02,217) .. (316.3,217) .. controls (315.58,217) and (315,216.42) .. (315,215.7) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 205; blue, 205 }  ,fill opacity=1 ] (326.5,98.7) .. controls (326.5,97.98) and (327.08,97.4) .. (327.8,97.4) .. controls (328.52,97.4) and (329.1,97.98) .. (329.1,98.7) .. controls (329.1,99.42) and (328.52,100) .. (327.8,100) .. controls (327.08,100) and (326.5,99.42) .. (326.5,98.7) -- cycle ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 205; blue, 205 }  ,fill opacity=1 ] (166.5,110.7) .. controls (166.5,109.98) and (167.08,109.4) .. (167.8,109.4) .. controls (168.52,109.4) and (169.1,109.98) .. (169.1,110.7) .. controls (169.1,111.42) and (168.52,112) .. (167.8,112) .. controls (167.08,112) and (166.5,111.42) .. (166.5,110.7) -- cycle ;
            		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (130.57,183.32) -- (416.77,183.32) ;
            		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (130.57,183.32) -- (173.35,137.15) ;
            	\\end{tikzpicture}
            \\end{center}"""
                % (f_expr)
            )

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = "\\True Với pha trăng mới ($F=0$), góc $\\alpha$ tương ứng bằng $0^\\circ$ hoặc $360^\\circ$"
            nb_da_1_s = "Với pha trăng mới ($F=0$), góc $\\alpha$ tương ứng bằng $90^\\circ$ hoặc $270^\\circ$"
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = """Với pha trăng mới $F = 0$, ta có $F = \\dfrac{1}{2}(1 - \\cos \\alpha) = 0 \\Leftrightarrow \\cos \\alpha = 1 \\Leftrightarrow \\alpha = 0^\\circ$ hoặc $\\alpha = 360^\\circ$."""

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = "\\True Với pha trăng tròn ($F=1$), góc $\\alpha$ tương ứng bằng $180^\\circ$"
            th_da_1_s = "\\True" if False else "Với pha trăng tròn ($F=1$), góc $\\alpha$ tương ứng bằng $0^\\circ$"
            th_da_1_s_alt = "Với pha trăng tròn ($F=1$), góc $\\alpha$ tương ứng bằng $0^\\circ$"
            list_th_da_1 = [th_da_1_d, th_da_1_s_alt]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = """Với pha trăng tròn $F = 1$, ta có $F = \\dfrac{1}{2}(1 - \\cos \\alpha) = 1 \\Leftrightarrow \\cos \\alpha = -1 \\Leftrightarrow \\alpha = 180^\\circ$."""

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = "\\True Với pha trăng bán nguyệt ($F=0,5$), góc $\\alpha$ tương ứng bằng $90^\\circ$ hoặc $270^\\circ$"
            vd_da_1_s = "Với pha trăng bán nguyệt ($F=0,5$), góc $\\alpha$ tương ứng bằng $60^\\circ$ hoặc $300^\\circ$"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = """Với pha trăng bán nguyệt $F = 0,5$, ta có $F = \\dfrac{1}{2}(1 - \\cos \\alpha) = 0,5 \\Leftrightarrow 1 - \\cos \\alpha = 1 \\Leftrightarrow \\cos \\alpha = 0 \\Leftrightarrow \\alpha = 90^\\circ$ hoặc $\\alpha = 270^\\circ$."""

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = "\\True Với pha trăng lưỡi liềm ($F=0,25$), góc $\\alpha$ tương ứng bằng $60^\\circ$ hoặc $300^\\circ$"
            vdc_da_1_s = "Với pha trăng lưỡi liềm ($F=0,25$), góc $\\alpha$ tương ứng bằng $45^\\circ$ hoặc $315^\\circ$"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = """Với pha trăng lưỡi liềm $F = 0,25$, ta có $F = \\dfrac{1}{2}(1 - \\cos \\alpha) = 0,25 \\Leftrightarrow 1 - \\cos \\alpha = 0,5 \\Leftrightarrow \\cos \\alpha = 0,5 \\Leftrightarrow \\alpha = 60^\\circ$ hoặc $\\alpha = 300^\\circ$."""

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum("\\True" in ans for ans in answers)


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
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi)
                + "\n\\choiceTFn \n"
                "{" + str(shuffled_answers_nb[0]) + "}\n"
                "{" + str(shuffled_answers_th[0]) + "}\n"
                "{" + str(shuffled_answers_vd[0]) + "}\n"
                "{" + str(shuffled_answers_vdc[0]) + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + str(shuffled_solutions_nb[0]) + "\n"
                "\\item " + str(shuffled_solutions_th[0]) + "\n"
                "\\item " + str(shuffled_solutions_vd[0]) + "\n"
                "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n \\end{minipage}\n\n")
            return content

