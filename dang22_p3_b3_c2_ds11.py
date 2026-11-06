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


def bt_dang22_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random đường kính D
                list_D = [1, 2, 4, 5, 8]
                D = random.choice(list_D)

                # Tính toán
                # Bán kính ban đầu R = D/2
                R = Rational(D, 2)
                # Bán kính đường tròn nội tiếp đầu tiên r1 = R/3 = D/6
                r1 = Rational(D, 6)


                kq_exact = math.pi * (D**2) / 18
                kq_round = Decimal(float(kq_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_round).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Tạo các đáp án sai
                kq_sai1 = Decimal(float(math.pi * (D**2) / 9)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_sai2 = Decimal(float(math.pi * (D**2) / 36)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_sai3 = Decimal(float(math.pi * (D**2) / 12)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_sai4 = Decimal(float(math.pi * (D**2) / 24)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_sai5 = Decimal(float(math.pi * (D**2) / 6)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                s = ['$%s$' % (str(kq_sai1).replace('.', ',')),
                     '$%s$' % (str(kq_sai2).replace('.', ',')),
                     '$%s$' % (str(kq_sai3).replace('.', ',')),
                     '$%s$' % (str(kq_sai4).replace('.', ',')),
                     '$%s$' % (str(kq_sai5).replace('.', ',')),
                    ]

                # Loại bỏ các đáp án sai trùng với đáp án đúng (nếu có, dù hiếm)
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Từ một tấm vải hình bán nguyệt đường kính $%s m$. Người nghệ nhân muốn vẽ một bức tranh trừu tượng bằng cách tô màu theo quy luật sau: \\\\
                1. Dựng hai hình bán nguyệt có đường kính bằng bán kính của hình bán nguyệt ban đầu, sau đó dựng một đường tròn tiếp xúc ngoài với 2 hình bán nguyệt mới và tiếp xúc trong với hình bán nguyệt cũ và tô màu cho nó. \\\\
                2. Lặp lại với hai hình bán nguyệt mới vừa dựng.
                \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [line width=1]  (215.53,32.13) .. controls (312.48,32.13) and (391.07,110.72) .. (391.07,207.67) -- (40,207.67) .. controls (40,110.72) and (118.59,32.13) .. (215.53,32.13) -- cycle ;
            		\\draw  [line width=1]  (127.67,119.8) .. controls (176.08,119.8) and (215.33,159.14) .. (215.33,207.67) -- (40,207.67) .. controls (40,159.14) and (79.25,119.8) .. (127.67,119.8) -- cycle ;
            		\\draw  [line width=1]  (303.2,119.8) .. controls (351.73,119.8) and (391.07,159.14) .. (391.07,207.67) -- (215.33,207.67) .. controls (215.33,159.14) and (254.67,119.8) .. (303.2,119.8) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (157.6,90.07) .. controls (157.6,58.07) and (183.54,32.13) .. (215.53,32.13) .. controls (247.53,32.13) and (273.47,58.07) .. (273.47,90.07) .. controls (273.47,122.06) and (247.53,148) .. (215.53,148) .. controls (183.54,148) and (157.6,122.06) .. (157.6,90.07) -- cycle ;
            		\\draw  [line width=1]  (127.77,120.4) .. controls (175.69,120.4) and (214.53,159.25) .. (214.53,207.17) -- (41,207.17) .. controls (41,159.25) and (79.85,120.4) .. (127.77,120.4) -- cycle ;
            		\\draw  [line width=1]  (84.33,163.73) .. controls (108.27,163.73) and (127.67,183.18) .. (127.67,207.17) -- (41,207.17) .. controls (41,183.18) and (60.4,163.73) .. (84.33,163.73) -- cycle ;
            		\\draw  [line width=1]  (171.1,163.73) .. controls (195.09,163.73) and (214.53,183.18) .. (214.53,207.17) -- (127.67,207.17) .. controls (127.67,183.18) and (147.11,163.73) .. (171.1,163.73) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (99.13,149.04) .. controls (99.13,133.22) and (111.95,120.4) .. (127.77,120.4) .. controls (143.58,120.4) and (156.4,133.22) .. (156.4,149.04) .. controls (156.4,164.85) and (143.58,177.67) .. (127.77,177.67) .. controls (111.95,177.67) and (99.13,164.85) .. (99.13,149.04) -- cycle ;
            		\\draw  [line width=1]  (303.77,119.4) .. controls (351.69,119.4) and (390.53,158.25) .. (390.53,206.17) -- (217,206.17) .. controls (217,158.25) and (255.85,119.4) .. (303.77,119.4) -- cycle ;
            		\\draw  [line width=1]  (260.33,162.73) .. controls (284.27,162.73) and (303.67,182.18) .. (303.67,206.17) -- (217,206.17) .. controls (217,182.18) and (236.4,162.73) .. (260.33,162.73) -- cycle ;
            		\\draw  [line width=1]  (347.1,162.73) .. controls (371.09,162.73) and (390.53,182.18) .. (390.53,206.17) -- (303.67,206.17) .. controls (303.67,182.18) and (323.11,162.73) .. (347.1,162.73) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (275.13,148.04) .. controls (275.13,132.22) and (287.95,119.4) .. (303.77,119.4) .. controls (319.58,119.4) and (332.4,132.22) .. (332.4,148.04) .. controls (332.4,163.85) and (319.58,176.67) .. (303.77,176.67) .. controls (287.95,176.67) and (275.13,163.85) .. (275.13,148.04) -- cycle ;
            		\\draw  [line width=1]  (83.8,163.87) .. controls (107.44,163.87) and (126.6,183.03) .. (126.6,206.67) -- (41,206.67) .. controls (41,183.03) and (60.16,163.87) .. (83.8,163.87) -- cycle ;
            		\\draw  [line width=1]  (62.38,185.24) .. controls (74.18,185.24) and (83.75,194.83) .. (83.75,206.67) -- (41,206.67) .. controls (41,194.83) and (50.57,185.24) .. (62.38,185.24) -- cycle ;
            		\\draw  [line width=1]  (105.18,185.24) .. controls (117.01,185.24) and (126.6,194.83) .. (126.6,206.67) -- (83.75,206.67) .. controls (83.75,194.83) and (93.34,185.24) .. (105.18,185.24) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (69.67,177.99) .. controls (69.67,170.19) and (76,163.87) .. (83.8,163.87) .. controls (91.6,163.87) and (97.93,170.19) .. (97.93,177.99) .. controls (97.93,185.79) and (91.6,192.12) .. (83.8,192.12) .. controls (76,192.12) and (69.67,185.79) .. (69.67,177.99) -- cycle ;
            		\\draw  [line width=1]  (170.8,163.87) .. controls (194.44,163.87) and (213.6,183.03) .. (213.6,206.67) -- (128,206.67) .. controls (128,183.03) and (147.16,163.87) .. (170.8,163.87) -- cycle ;
            		\\draw  [line width=1]  (149.38,185.24) .. controls (161.18,185.24) and (170.75,194.83) .. (170.75,206.67) -- (128,206.67) .. controls (128,194.83) and (137.57,185.24) .. (149.38,185.24) -- cycle ;
            		\\draw  [line width=1]  (192.18,185.24) .. controls (204.01,185.24) and (213.6,194.83) .. (213.6,206.67) -- (170.75,206.67) .. controls (170.75,194.83) and (180.34,185.24) .. (192.18,185.24) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (156.67,177.99) .. controls (156.67,170.19) and (163,163.87) .. (170.8,163.87) .. controls (178.6,163.87) and (184.93,170.19) .. (184.93,177.99) .. controls (184.93,185.79) and (178.6,192.12) .. (170.8,192.12) .. controls (163,192.12) and (156.67,185.79) .. (156.67,177.99) -- cycle ;
            		\\draw  [line width=1]  (260.3,163.37) .. controls (283.94,163.37) and (303.1,182.53) .. (303.1,206.17) -- (217.5,206.17) .. controls (217.5,182.53) and (236.66,163.37) .. (260.3,163.37) -- cycle ;
            		\\draw  [line width=1]  (238.88,184.74) .. controls (250.68,184.74) and (260.25,194.33) .. (260.25,206.17) -- (217.5,206.17) .. controls (217.5,194.33) and (227.07,184.74) .. (238.88,184.74) -- cycle ;
            		\\draw  [line width=1]  (281.68,184.74) .. controls (293.51,184.74) and (303.1,194.33) .. (303.1,206.17) -- (260.25,206.17) .. controls (260.25,194.33) and (269.84,184.74) .. (281.68,184.74) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (246.17,177.49) .. controls (246.17,169.69) and (252.5,163.37) .. (260.3,163.37) .. controls (268.1,163.37) and (274.43,169.69) .. (274.43,177.49) .. controls (274.43,185.29) and (268.1,191.62) .. (260.3,191.62) .. controls (252.5,191.62) and (246.17,185.29) .. (246.17,177.49) -- cycle ;
            		\\draw  [line width=1]  (347.8,163.37) .. controls (371.44,163.37) and (390.6,182.53) .. (390.6,206.17) -- (305,206.17) .. controls (305,182.53) and (324.16,163.37) .. (347.8,163.37) -- cycle ;
            		\\draw  [line width=1]  (326.38,184.74) .. controls (338.18,184.74) and (347.75,194.33) .. (347.75,206.17) -- (305,206.17) .. controls (305,194.33) and (314.57,184.74) .. (326.38,184.74) -- cycle ;
            		\\draw  [line width=1]  (369.18,184.74) .. controls (381.01,184.74) and (390.6,194.33) .. (390.6,206.17) -- (347.75,206.17) .. controls (347.75,194.33) and (357.34,184.74) .. (369.18,184.74) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (333.67,177.49) .. controls (333.67,169.69) and (340,163.37) .. (347.8,163.37) .. controls (355.6,163.37) and (361.93,169.69) .. (361.93,177.49) .. controls (361.93,185.29) and (355.6,191.62) .. (347.8,191.62) .. controls (340,191.62) and (333.67,185.29) .. (333.67,177.49) -- cycle ;
            		\\draw  [line width=1]  (62.55,185.62) .. controls (73.9,185.62) and (83.1,194.82) .. (83.1,206.17) -- (42,206.17) .. controls (42,194.82) and (51.2,185.62) .. (62.55,185.62) -- cycle ;
            		\\draw  [line width=1]  (52.26,195.88) .. controls (57.93,195.88) and (62.53,200.49) .. (62.53,206.17) -- (42,206.17) .. controls (42,200.49) and (46.6,195.88) .. (52.26,195.88) -- cycle ;
            		\\draw  [line width=1]  (72.81,195.88) .. controls (78.49,195.88) and (83.1,200.49) .. (83.1,206.17) -- (62.53,206.17) .. controls (62.53,200.49) and (67.13,195.88) .. (72.81,195.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (55.77,192.4) .. controls (55.77,188.65) and (58.8,185.62) .. (62.55,185.62) .. controls (66.3,185.62) and (69.33,188.65) .. (69.33,192.4) .. controls (69.33,196.14) and (66.3,199.18) .. (62.55,199.18) .. controls (58.8,199.18) and (55.77,196.14) .. (55.77,192.4) -- cycle ;
            		\\draw  [line width=1]  (105.55,184.62) .. controls (116.9,184.62) and (126.1,193.82) .. (126.1,205.17) -- (85,205.17) .. controls (85,193.82) and (94.2,184.62) .. (105.55,184.62) -- cycle ;
            		\\draw  [line width=1]  (95.26,194.88) .. controls (100.93,194.88) and (105.53,199.49) .. (105.53,205.17) -- (85,205.17) .. controls (85,199.49) and (89.6,194.88) .. (95.26,194.88) -- cycle ;
            		\\draw  [line width=1]  (115.81,194.88) .. controls (121.49,194.88) and (126.1,199.49) .. (126.1,205.17) -- (105.53,205.17) .. controls (105.53,199.49) and (110.13,194.88) .. (115.81,194.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (98.77,191.4) .. controls (98.77,187.65) and (101.8,184.62) .. (105.55,184.62) .. controls (109.3,184.62) and (112.33,187.65) .. (112.33,191.4) .. controls (112.33,195.14) and (109.3,198.18) .. (105.55,198.18) .. controls (101.8,198.18) and (98.77,195.14) .. (98.77,191.4) -- cycle ;
            		\\draw  [line width=1]  (149.55,185.12) .. controls (160.9,185.12) and (170.1,194.32) .. (170.1,205.67) -- (129,205.67) .. controls (129,194.32) and (138.2,185.12) .. (149.55,185.12) -- cycle ;
            		\\draw  [line width=1]  (139.26,195.38) .. controls (144.93,195.38) and (149.53,199.99) .. (149.53,205.67) -- (129,205.67) .. controls (129,199.99) and (133.6,195.38) .. (139.26,195.38) -- cycle ;
            		\\draw  [line width=1]  (159.81,195.38) .. controls (165.49,195.38) and (170.1,199.99) .. (170.1,205.67) -- (149.53,205.67) .. controls (149.53,199.99) and (154.13,195.38) .. (159.81,195.38) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (142.77,191.9) .. controls (142.77,188.15) and (145.8,185.12) .. (149.55,185.12) .. controls (153.3,185.12) and (156.33,188.15) .. (156.33,191.9) .. controls (156.33,195.64) and (153.3,198.68) .. (149.55,198.68) .. controls (145.8,198.68) and (142.77,195.64) .. (142.77,191.9) -- cycle ;
            		\\draw  [line width=1]  (192.55,185.62) .. controls (203.9,185.62) and (213.1,194.82) .. (213.1,206.17) -- (172,206.17) .. controls (172,194.82) and (181.2,185.62) .. (192.55,185.62) -- cycle ;
            		\\draw  [line width=1]  (182.26,195.88) .. controls (187.93,195.88) and (192.53,200.49) .. (192.53,206.17) -- (172,206.17) .. controls (172,200.49) and (176.6,195.88) .. (182.26,195.88) -- cycle ;
            		\\draw  [line width=1]  (202.81,195.88) .. controls (208.49,195.88) and (213.1,200.49) .. (213.1,206.17) -- (192.53,206.17) .. controls (192.53,200.49) and (197.13,195.88) .. (202.81,195.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (185.77,192.4) .. controls (185.77,188.65) and (188.8,185.62) .. (192.55,185.62) .. controls (196.3,185.62) and (199.33,188.65) .. (199.33,192.4) .. controls (199.33,196.14) and (196.3,199.18) .. (192.55,199.18) .. controls (188.8,199.18) and (185.77,196.14) .. (185.77,192.4) -- cycle ;
            		\\draw  [line width=1]  (240.05,184.62) .. controls (251.4,184.62) and (260.6,193.82) .. (260.6,205.17) -- (219.5,205.17) .. controls (219.5,193.82) and (228.7,184.62) .. (240.05,184.62) -- cycle ;
            		\\draw  [line width=1]  (229.76,194.88) .. controls (235.43,194.88) and (240.03,199.49) .. (240.03,205.17) -- (219.5,205.17) .. controls (219.5,199.49) and (224.1,194.88) .. (229.76,194.88) -- cycle ;
            		\\draw  [line width=1]  (250.31,194.88) .. controls (255.99,194.88) and (260.6,199.49) .. (260.6,205.17) -- (240.03,205.17) .. controls (240.03,199.49) and (244.63,194.88) .. (250.31,194.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (233.27,191.4) .. controls (233.27,187.65) and (236.3,184.62) .. (240.05,184.62) .. controls (243.8,184.62) and (246.83,187.65) .. (246.83,191.4) .. controls (246.83,195.14) and (243.8,198.18) .. (240.05,198.18) .. controls (236.3,198.18) and (233.27,195.14) .. (233.27,191.4) -- cycle ;
            		\\draw  [line width=1]  (282.05,185.62) .. controls (293.4,185.62) and (302.6,194.82) .. (302.6,206.17) -- (261.5,206.17) .. controls (261.5,194.82) and (270.7,185.62) .. (282.05,185.62) -- cycle ;
            		\\draw  [line width=1]  (271.76,195.88) .. controls (277.43,195.88) and (282.03,200.49) .. (282.03,206.17) -- (261.5,206.17) .. controls (261.5,200.49) and (266.1,195.88) .. (271.76,195.88) -- cycle ;
            		\\draw  [line width=1]  (292.31,195.88) .. controls (297.99,195.88) and (302.6,200.49) .. (302.6,206.17) -- (282.03,206.17) .. controls (282.03,200.49) and (286.63,195.88) .. (292.31,195.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (275.27,192.4) .. controls (275.27,188.65) and (278.3,185.62) .. (282.05,185.62) .. controls (285.8,185.62) and (288.83,188.65) .. (288.83,192.4) .. controls (288.83,196.14) and (285.8,199.18) .. (282.05,199.18) .. controls (278.3,199.18) and (275.27,196.14) .. (275.27,192.4) -- cycle ;
            		\\draw  [line width=1]  (326.55,184.62) .. controls (337.9,184.62) and (347.1,193.82) .. (347.1,205.17) -- (306,205.17) .. controls (306,193.82) and (315.2,184.62) .. (326.55,184.62) -- cycle ;
            		\\draw  [line width=1]  (316.26,194.88) .. controls (321.93,194.88) and (326.53,199.49) .. (326.53,205.17) -- (306,205.17) .. controls (306,199.49) and (310.6,194.88) .. (316.26,194.88) -- cycle ;
            		\\draw  [line width=1]  (336.81,194.88) .. controls (342.49,194.88) and (347.1,199.49) .. (347.1,205.17) -- (326.53,205.17) .. controls (326.53,199.49) and (331.13,194.88) .. (336.81,194.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (319.77,191.4) .. controls (319.77,187.65) and (322.8,184.62) .. (326.55,184.62) .. controls (330.3,184.62) and (333.33,187.65) .. (333.33,191.4) .. controls (333.33,195.14) and (330.3,198.18) .. (326.55,198.18) .. controls (322.8,198.18) and (319.77,195.14) .. (319.77,191.4) -- cycle ;
            		\\draw  [line width=1]  (369.05,184.62) .. controls (380.4,184.62) and (389.6,193.82) .. (389.6,205.17) -- (348.5,205.17) .. controls (348.5,193.82) and (357.7,184.62) .. (369.05,184.62) -- cycle ;
            		\\draw  [line width=1]  (358.76,194.88) .. controls (364.43,194.88) and (369.03,199.49) .. (369.03,205.17) -- (348.5,205.17) .. controls (348.5,199.49) and (353.1,194.88) .. (358.76,194.88) -- cycle ;
            		\\draw  [line width=1]  (379.31,194.88) .. controls (384.99,194.88) and (389.6,199.49) .. (389.6,205.17) -- (369.03,205.17) .. controls (369.03,199.49) and (373.63,194.88) .. (379.31,194.88) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=1]  (362.27,191.4) .. controls (362.27,187.65) and (365.3,184.62) .. (369.05,184.62) .. controls (372.8,184.62) and (375.83,187.65) .. (375.83,191.4) .. controls (375.83,195.14) and (372.8,198.18) .. (369.05,198.18) .. controls (365.3,198.18) and (362.27,195.14) .. (362.27,191.4) -- cycle ;
            	\\end{tikzpicture}
            \\end{center}
                Tổng diện tích phần tô màu là bao nhiêu $m^2$? (Làm tròn đến hàng phần chục).'''
                                 % (latex(D)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $R$ là bán kính hình bán nguyệt ban đầu. Ta có $R = \\frac{%s}{2}$. \\\\
                Giả sử đường tròn được tô màu ở bước 1 có tâm $I$, bán kính $r_1$. \\\\
                Gọi $O$ là tâm hình bán nguyệt ban đầu, $O_1, O_2$ là tâm của hai hình bán nguyệt mới. \\\\
                Ta có $O_1O_2 = 2 \\cdot \\frac{R}{2} = R$. \\\\
                Tam giác $IO_1O_2$ cân tại $I$, có đường cao $IO$. \\\\
                Ta có: $IO_1 = \\frac{R}{2} + r_1$; $IO = R - r_1$; $OO_1 = \\frac{R}{2}$. \\\\
                Trong tam giác vuông $IOO_1$: $IO_1^2 = IO^2 + OO_1^2 \\Leftrightarrow \\left(\\frac{R}{2} + r_1\\right)^2 = (R - r_1)^2 + \\left(\\frac{R}{2}\\right)^2$. \\\\
                Giải phương trình ta được $r_1 = \\frac{R}{3} = \\frac{%s}{6}$. \\\\
                Diện tích hình tròn đầu tiên được tô màu là $S_1 = \\pi r_1^2 = \\pi \\left(\\frac{%s}{6}\\right)^2$. \\\\
                Ở bước 2, tại mỗi hình bán nguyệt mới (bán kính $\\frac{R}{2}$), ta dựng được một đường tròn tô màu có bán kính $r_2 = \\frac{1}{3} \\cdot \\frac{R}{2} = \\frac{r_1}{2}$. \\\\
                Có 2 hình tròn như vậy, tổng diện tích phần tô màu ở bước 2 là $S_2 = 2 \\cdot \\pi r_2^2 = 2 \\cdot \\pi \\left(\\frac{r_1}{2}\\right)^2 = \\frac{1}{2} \\pi r_1^2 = \\frac{1}{2} S_1$. \\\\
                Tương tự, ở bước 3, có $2^2$ đường tròn bán kính $r_3 = \\frac{r_2}{2} = \\frac{r_1}{4}$. Tổng diện tích $S_3 = 4 \\cdot \\pi \\left(\\frac{r_1}{4}\\right)^2 = \\frac{1}{4} \\pi r_1^2 = \\frac{1}{4} S_1$. \\\\
                Quá trình này lặp lại vô hạn lần, tổng diện tích phần tô màu lập thành một cấp số nhân lùi vô hạn có số hạng đầu $u_1 = S_1$ và công bội $q = \\frac{1}{2}$. \\\\
                Tổng diện tích phần tô màu là: \\\\
                $S = S_1 + S_2 + S_3 + \\dots = \\frac{S_1}{1 - q} = \\frac{\\pi \\left(\\frac{%s}{6}\\right)^2}{1 - \\frac{1}{2}} = 2 \\pi \\left(\\frac{%s}{6}\\right)^2 = \\frac{%s^2 \\pi}{18} \\approx %s$ ($m^2$).'''
                           % (latex(D), latex(D), latex(D), latex(D), latex(D), latex(D), str(kq_round).replace('.', ',')))
            dapan='\\shortans[0]{$%s$}\n'%(str(kq_round).replace('.', ','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

