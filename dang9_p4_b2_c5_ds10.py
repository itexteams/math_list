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


def bt_dang9_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng chữ cái cho seri (VD: 15 đến 24)
                n_letters = random.randint(15, 24)

                # Random chữ số tận cùng của tổng. Tránh 0 và 5 để đảm bảo số lượng cặp x,y (x khác y) luôn bằng 10.
                k_end = random.choice([1, 2, 3, 4, 6, 7, 8, 9])

                # Random số biển số cần chọn ra
                choose_num = random.choice([2, 3])

                # Sinh danh sách các cặp (x, y) sao cho (4x + y) mod 10 == k_end
                pairs_list = []
                for x_val in range(10):
                    y_val = (k_end - 4 * x_val) % 10
                    pairs_list.append(f"\\left({x_val}; {y_val}\\right)")
                pairs_str = "; ".join(pairs_list)

                # Tính toán kết quả
                total_plates = n_letters * 10 * 5
                result = math.comb(total_plates, choose_num)
                # Các đáp án trắc nghiệm
                kq = str(result)
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                wrong_answers = set()
                # Lỗi 1: Quên nhân 5 (các trường hợp hoán vị)
                wrong_answers.add(math.comb(n_letters * 10, choose_num))
                # Lỗi 2: Tính chỉnh hợp thay vì tổ hợp
                if total_plates > choose_num:
                    wrong_answers.add(math.perm(total_plates, choose_num))
                # Lỗi 3: Chỉ tính tổng số biển số, không tính tổ hợp chập choose_num
                wrong_answers.add(total_plates)
                # Lỗi 4: Lỗi sai cộng trừ cơ học
                wrong_answers.add(result + random.randint(1, 5) * 100)
                wrong_answers.add(abs(result - random.randint(1, 5) * 100))
                # Lỗi 5: Sai số chập (VD cần chập 3 thì tính chập 2)
                wrong_answers.add(math.comb(total_plates, 2 if choose_num == 3 else 3))

                # Lọc bỏ nếu vô tình trùng đáp án đúng và chọn ra 3 đáp án sai
                wrong_list = [val for val in wrong_answers if val != result and val > 0]
                random.shuffle(wrong_list)

                s = ['$%s$'%(str(wrong_list[0])),
                     '$%s$'%(str(wrong_list[1])),
                     '$%s$'%(str(wrong_list[2])),
                     '$%s$'%(str(wrong_list[3])),
                     '$%s$'%(str(wrong_list[4]))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\tikzset {_2gusq9u8j/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-84 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_axdfk9hna}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            	rgb(37.5bp)=(0.82,0.01,0.11);
            	rgb(44.498885018484934bp)=(1,0.98,0.81);
            	rgb(52.90960584368025bp)=(0.82,0.01,0.11);
            	rgb(100bp)=(0.82,0.01,0.11)}
            \tikzset {_tycmiwrlc/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-84 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_m2jtu02oo}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            	rgb(37.5bp)=(0.82,0.01,0.11);
            	rgb(44.498885018484934bp)=(1,0.98,0.81);
            	rgb(52.90960584368025bp)=(0.82,0.01,0.11);
            	rgb(100bp)=(0.82,0.01,0.11)}
            \tikzset {_v5u29bty2/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_xlu7f0ud2}{150bp}{rgb(0bp)=(0,0,0);
            	rgb(48.089288984026226bp)=(0,0,0);
            	rgb(62.5bp)=(0.82,0.01,0.11);
            	rgb(100bp)=(0.82,0.01,0.11)}
            \tikzset{_xh7t5w7d2/.code = {\pgfsetadditionalshadetransform{\pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 } }}}
            \pgfdeclarehorizontalshading{_o9lyuvxfz} {150bp} {color(0bp)=(transparent!10);
            	color(48.089288984026226bp)=(transparent!10);
            	color(62.5bp)=(transparent!0);
            	color(100bp)=(transparent!0) } 
            \pgfdeclarefading{_a8kqtn1nv}{\tikz \fill[shading=_o9lyuvxfz,_xh7t5w7d2] (0,0) rectangle (50bp,50bp); } 
            \tikzset {_8w3ideb9j/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_lg2elfqee}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            	rgb(37.5bp)=(0.82,0.01,0.11);
            	rgb(51.64285932268415bp)=(0,0,0);
            	rgb(100bp)=(0,0,0)}
            \tikzset{_lazxkdd1t/.code = {\pgfsetadditionalshadetransform{\pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 } }}}
            \pgfdeclarehorizontalshading{_tt1w0jztr} {150bp} {color(0bp)=(transparent!0);
            	color(37.5bp)=(transparent!0);
            	color(51.64285932268415bp)=(transparent!10);
            	color(100bp)=(transparent!10) } 
            \pgfdeclarefading{_j9wvquspf}{\tikz \fill[shading=_tt1w0jztr,_lazxkdd1t] (0,0) rectangle (50bp,50bp); } 
            \tikzset {_1jdlce4pw/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_h2v5kbrwa}{150bp}{rgb(0bp)=(0.35,0.04,0.08);
            	rgb(37.5bp)=(0.35,0.04,0.08);
            	rgb(62.5bp)=(0.82,0.01,0.11);
            	rgb(100bp)=(0.82,0.01,0.11)}
            \tikzset {_rqr9vf2g6/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_1z1c6stsa}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            	rgb(37.5bp)=(0.82,0.01,0.11);
            	rgb(62.5bp)=(0.35,0.04,0.08);
            	rgb(100bp)=(0.35,0.04,0.08)}
            \tikzset{every picture/.style={line width=0.75pt}} 
            \begin{center} \scalebox{1.5}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.73 ] (262.2,135.75) .. controls (262.2,132.47) and (264.86,129.81) .. (268.15,129.81) -- (399.75,129.81) .. controls (403.04,129.81) and (405.7,132.47) .. (405.7,135.75) -- (405.7,135.75) .. controls (405.7,139.04) and (403.04,141.7) .. (399.75,141.7) -- (268.15,141.7) .. controls (264.86,141.7) and (262.2,139.04) .. (262.2,135.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.5 ] (253.1,137.87) .. controls (253.1,133.58) and (256.58,130.1) .. (260.87,130.1) -- (403.82,130.1) .. controls (408.12,130.1) and (411.6,133.58) .. (411.6,137.87) -- (411.6,137.87) .. controls (411.6,142.17) and (408.12,145.65) .. (403.82,145.65) -- (260.87,145.65) .. controls (256.58,145.65) and (253.1,142.17) .. (253.1,137.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (254.95,109.28) .. controls (254.83,106.11) and (257.3,103.44) .. (260.48,103.32) -- (272.74,102.85) .. controls (275.92,102.73) and (278.59,105.21) .. (278.71,108.38) -- (279.71,134.78) .. controls (279.83,137.96) and (277.35,140.63) .. (274.18,140.75) -- (261.91,141.22) .. controls (258.74,141.34) and (256.07,138.86) .. (255.95,135.68) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.17 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (256.6,74.4) .. controls (258.39,74.17) and (263.35,72.65) .. (267.62,73.07) .. controls (267.7,74.4) and (268.45,76.65) .. (268.39,77.99) .. controls (287.14,79.21) and (277.1,88.9) .. (266.85,81.75) .. controls (262.92,81.67) and (258.76,81.2) .. (255.6,80.15) .. controls (252.85,78.49) and (253.56,75.92) .. (256.6,74.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (409.55,109.63) .. controls (409.69,106.21) and (407.04,103.33) .. (403.63,103.18) -- (390.45,102.62) .. controls (387.04,102.48) and (384.15,105.13) .. (384.01,108.54) -- (382.92,134.07) .. controls (382.77,137.48) and (385.42,140.37) .. (388.83,140.51) -- (402.02,141.08) .. controls (405.43,141.22) and (408.32,138.57) .. (408.46,135.16) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.17 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (404.02,72.4) .. controls (402.23,72.17) and (397.25,70.65) .. (392.97,71.07) .. controls (392.89,72.4) and (392.14,74.65) .. (392.2,75.99) .. controls (373.39,77.21) and (383.46,86.9) .. (393.74,79.75) .. controls (397.69,79.67) and (401.85,79.2) .. (405.03,78.15) .. controls (407.79,76.49) and (407.07,73.92) .. (404.02,72.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (292.05,53.65) .. controls (329.55,50.4) and (332.3,51.15) .. (367.8,53.15) .. controls (375.55,57.65) and (383.04,66.09) .. (386.99,73.08) .. controls (388.82,76.32) and (390.91,79.03) .. (392.35,80.08) .. controls (396.2,82.89) and (403.21,86.83) .. (408.86,92.08) .. controls (411.27,110.46) and (412.46,135.01) .. (402.57,135.67) .. controls (385.7,136.79) and (368.2,138.21) .. (367.7,137.74) .. controls (365.69,135.87) and (354.78,134.85) .. (300.32,136.28) .. controls (298.22,136.59) and (296.73,137.14) .. (296.04,137.99) .. controls (282.78,136.79) and (267.04,137.46) .. (262.2,135.11) .. controls (256.93,132.54) and (253.52,121.94) .. (254.81,91.16) .. controls (258.54,87.68) and (264,83.7) .. (271.61,79.07) .. controls (272.41,77.18) and (273.35,75.23) .. (274.41,73.21) .. controls (278.29,65.9) and (284.21,59.29) .. (292.05,53.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (294.7,53.15) .. controls (323.2,51.15) and (335.95,50.65) .. (365.45,52.9) .. controls (370.7,57.15) and (372.95,59.9) .. (384.95,75.15) .. controls (376.45,75.4) and (291.2,76.65) .. (277.45,74.15) .. controls (288.45,56.65) and (291.55,55.15) .. (294.7,53.15) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (298.3,52.4) .. controls (326.8,50.4) and (334.3,50.15) .. (363.8,52.4) .. controls (369.05,56.65) and (378.3,68.4) .. (379.8,72.9) .. controls (384.55,80.15) and (283.8,78.4) .. (281.8,73.4) .. controls (287.3,63.4) and (295.15,54.4) .. (298.3,52.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (298.3,52.4) .. controls (326.8,50.4) and (334.3,50.15) .. (363.8,52.4) .. controls (369.05,56.65) and (365.55,51.4) .. (367.05,55.9) .. controls (330.8,55.9) and (331.05,55.15) .. (294.3,56.15) .. controls (299.8,46.15) and (295.15,54.4) .. (298.3,52.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (331.75,53.4) -- (335.05,53.4) -- (335.05,61.4) -- (331.75,61.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (322.05,59.9) .. controls (322.05,58.66) and (323.06,57.65) .. (324.3,57.65) -- (338.3,57.65) .. controls (339.54,57.65) and (340.55,58.66) .. (340.55,59.9) -- (340.55,59.9) .. controls (340.55,61.14) and (339.54,62.15) .. (338.3,62.15) -- (324.3,62.15) .. controls (323.06,62.15) and (322.05,61.14) .. (322.05,59.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (347.3,64.15) .. controls (352.05,63.4) and (357.12,63.43) .. (362.55,64.65) .. controls (364.05,66.65) and (361.81,70.13) .. (364.55,71.4) .. controls (366.9,71.33) and (367.97,73.18) .. (370.3,73.9) .. controls (372.31,79.59) and (367.05,74.65) .. (357.3,75.9) .. controls (345.7,75.36) and (331.47,76.03) .. (343.3,71.9) .. controls (344.9,67.7) and (342.48,66.56) .. (347.3,64.15) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (302.05,63.4) .. controls (306.8,62.65) and (311.87,62.68) .. (317.3,63.9) .. controls (318.8,65.9) and (316.56,69.38) .. (319.3,70.65) .. controls (321.65,70.58) and (322.72,72.43) .. (325.05,73.15) .. controls (327.06,78.84) and (321.8,73.9) .. (312.05,75.15) .. controls (300.45,74.61) and (286.22,75.28) .. (298.05,71.15) .. controls (299.65,66.95) and (297.23,65.81) .. (302.05,63.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (297.03,75.35) .. controls (298.24,71.59) and (303.26,68.83) .. (309.22,68.93) .. controls (315.54,69.04) and (320.69,72.34) .. (321.34,76.48) -- (318.54,76.65) .. controls (317.95,73.95) and (313.99,71.81) .. (309.17,71.72) .. controls (304.67,71.64) and (300.86,73.38) .. (299.82,75.79) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (296.55,93.7) .. controls (321.3,91.95) and (331.3,92.2) .. (373.3,93.7) .. controls (371.05,104.32) and (353.55,107.45) .. (334.05,106.95) .. controls (309.55,107.7) and (296.93,102.58) .. (296.55,93.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.56 ] (371.98,96.4) -- (368.03,99.83) -- (300.23,99.11) -- (296.35,95.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.56 ] (367.98,101.73) -- (358.9,105.02) -- (309.36,104.5) -- (300.35,101.01) -- cycle ;
            	\draw  [draw opacity=0][shading=_axdfk9hna,_2gusq9u8j] (275.7,73.65) .. controls (275.45,82.9) and (293.7,87.15) .. (294.45,101.9) .. controls (295.2,102.4) and (294.45,102.4) .. (286.45,95.15) .. controls (280.45,84.4) and (265.45,86.4) .. (275.7,73.65) -- cycle ;
            	\draw  [draw opacity=0][shading=_m2jtu02oo,_tycmiwrlc] (388.57,76.15) .. controls (388.82,85.4) and (370.65,89.65) .. (369.9,104.4) .. controls (369.15,104.9) and (369.9,104.9) .. (377.87,97.65) .. controls (383.84,86.9) and (398.78,88.9) .. (388.57,76.15) -- cycle ;
            	\draw  [draw opacity=0][shading=_xlu7f0ud2,_v5u29bty2,path fading= _a8kqtn1nv ,fading transform={xshift=2}] (265.6,113.6) .. controls (269.91,113.45) and (278.69,114.12) .. (289.59,115.48) .. controls (290.6,119.15) and (290.85,120.15) .. (295.35,131.56) .. controls (286.56,131.49) and (277.1,131.15) .. (269.6,128.15) .. controls (268.24,124.59) and (265.35,120.15) .. (265.6,113.6) -- cycle ;
            	\draw  [draw opacity=0][shading=_lg2elfqee,_8w3ideb9j,path fading= _j9wvquspf ,fading transform={xshift=2}] (402.53,114.6) .. controls (397.98,114.45) and (388.7,115.12) .. (377.18,116.48) .. controls (376.12,120.15) and (375.85,121.15) .. (371.1,132.56) .. controls (380.38,132.49) and (390.38,132.15) .. (398.31,129.15) .. controls (399.74,125.59) and (401,122.75) .. (402.53,114.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (295.75,119) .. controls (313.75,119) and (374,118.75) .. (369.75,119.5) .. controls (368.5,125.5) and (367,128.5) .. (364.05,130) .. controls (346.3,131.75) and (330.25,131) .. (304.55,131) .. controls (297.05,128) and (297.95,124.25) .. (295.75,119) -- cycle ;
            	\draw    (294.5,114.75) -- (297,122) ;
            	\draw    (371.25,115.75) -- (369,123) ;
            	\draw  [draw opacity=0][shading=_h2v5kbrwa,_1jdlce4pw] (254.62,106.5) .. controls (257.65,108.65) and (262.35,111.35) .. (265.6,113.6) .. controls (270.8,126.65) and (257.4,131.9) .. (303.41,131.76) .. controls (302.3,131.15) and (297.05,136.42) .. (296.04,137.99) .. controls (281.54,137.99) and (261.4,138.9) .. (257.44,131.53) .. controls (254.76,122.26) and (254.3,113.4) .. (254.62,106.5) -- cycle ;
            	\draw  [draw opacity=0][shading=_1z1c6stsa,_rqr9vf2g6] (410.4,107.65) .. controls (407.33,109.57) and (405.83,112.59) .. (402.53,114.6) .. controls (398.7,130.15) and (402.7,133.15) .. (360.04,132.17) .. controls (361.17,131.63) and (366.48,136.34) .. (367.51,137.74) .. controls (382.19,137.74) and (402.69,139.73) .. (406.7,133.15) .. controls (410.95,126.15) and (410.15,114.4) .. (410.4,107.65) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (265.6,113.6) .. controls (267.15,126.4) and (267.4,125.4) .. (269.6,128.15) .. controls (271.8,130.9) and (282.65,131.65) .. (301.9,132.4) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (402.53,114.6) .. controls (400.89,127.4) and (400.63,126.4) .. (398.31,129.15) .. controls (395.99,131.9) and (384.54,132.65) .. (364.23,133.4) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 210; blue, 210 }  ,fill opacity=1 ] (264.55,86.9) .. controls (270.9,86.55) and (276.5,89.19) .. (284.65,92.9) .. controls (287.9,96.65) and (289.9,98.9) .. (292.3,104.4) .. controls (277.3,102.9) and (273.44,104.15) .. (264.55,100.9) .. controls (263.85,95.83) and (262.84,90.92) .. (264.55,86.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 210; blue, 210 }  ,fill opacity=1 ] (403.63,89.18) .. controls (397.35,88.84) and (390.21,91.69) .. (382.15,95.4) .. controls (380.15,98.4) and (378.9,100.4) .. (376.19,106.68) .. controls (391.02,105.18) and (394.84,106.43) .. (403.63,103.18) .. controls (404.32,98.11) and (405.32,93.21) .. (403.63,89.18) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.13 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (381.4,100.32) .. controls (381.4,97.88) and (383.57,95.9) .. (386.25,95.9) .. controls (388.93,95.9) and (391.1,97.88) .. (391.1,100.32) .. controls (391.1,102.77) and (388.93,104.75) .. (386.25,104.75) .. controls (383.57,104.75) and (381.4,102.77) .. (381.4,100.32) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.13 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (276.15,97.82) .. controls (276.15,95.38) and (278.32,93.4) .. (281,93.4) .. controls (283.68,93.4) and (285.85,95.38) .. (285.85,97.82) .. controls (285.85,100.27) and (283.68,102.25) .. (281,102.25) .. controls (278.32,102.25) and (276.15,100.27) .. (276.15,97.82) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.13 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (391.4,97.07) .. controls (391.4,94.63) and (393.57,92.65) .. (396.25,92.65) .. controls (398.93,92.65) and (401.1,94.63) .. (401.1,97.07) .. controls (401.1,99.52) and (398.93,101.5) .. (396.25,101.5) .. controls (393.57,101.5) and (391.4,99.52) .. (391.4,97.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.13 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (265.4,94.07) .. controls (265.4,91.63) and (267.57,89.65) .. (270.25,89.65) .. controls (272.93,89.65) and (275.1,91.63) .. (275.1,94.07) .. controls (275.1,96.52) and (272.93,98.5) .. (270.25,98.5) .. controls (267.57,98.5) and (265.4,96.52) .. (265.4,94.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 234; green, 225; blue, 225 }  ,fill opacity=1 ] (309.05,116.3) .. controls (309.05,115.11) and (310.01,114.15) .. (311.2,114.15) -- (354.55,114.15) .. controls (355.74,114.15) and (356.7,115.11) .. (356.7,116.3) -- (356.7,122.5) .. controls (356.7,123.69) and (355.74,124.65) .. (354.55,124.65) -- (311.2,124.65) .. controls (310.01,124.65) and (309.05,123.69) .. (309.05,122.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 238; blue, 192 }  ,fill opacity=0.26 ] (262.7,90.9) -- (265.6,113.6) -- (294.5,116.15) -- (292.3,104.4) -- (284.65,92.9) -- (265.75,86.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 238; blue, 192 }  ,fill opacity=0.26 ] (405.36,91.9) -- (402.53,114.6) -- (373.45,116.4) -- (376.51,105.4) -- (383.96,93.9) -- (403.63,89.18) -- cycle ;
            	\draw [color={rgb, 255:red, 123; green, 9; blue, 23 }  ,draw opacity=0.51 ]   (264.55,100.9) .. controls (271.95,103.65) and (285.7,103.9) .. (292.3,104.4) ;
            	\draw [color={rgb, 255:red, 123; green, 9; blue, 23 }  ,draw opacity=0.51 ]   (376.19,106.68) .. controls (388.45,106.4) and (397.2,105.4) .. (403.63,103.18) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.19 ] (330.2,77.4) -- (329.7,91.9) -- (302.32,92.54) -- (319.7,78.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.19 ] (304.7,55.9) -- (350.2,77.15) -- (318.54,76.65) -- (297.3,55.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.19 ] (324.88,55.15) -- (370.38,76.4) -- (331.7,76.4) -- (317.48,54.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.19 ] (376.38,76.65) -- (373.3,93.7) -- (340.7,92.15) -- (368.98,76.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (255.95,103.9) -- (265.6,113.6) -- (254.62,106.5) -- (254.81,91.16) -- cycle ;
            	\draw [color={rgb, 255:red, 88; green, 10; blue, 10 }  ,draw opacity=0.63 ]   (297.7,97.65) .. controls (296.58,104.61) and (316.61,109.04) .. (335.2,109.15) .. controls (353.79,109.26) and (372.7,104.4) .. (373.3,93.7) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (264.2,75.65) -- (255.7,75.65) -- (266.31,74.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (398.2,73.9) -- (394.95,72.15) -- (404.2,73.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (309.5,114.65) -- (314.2,114.65) -- (314.2,124.4) -- (309.5,124.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (311.85,117.53) -- (312.39,118.72) -- (313.6,118.91) -- (312.73,119.83) -- (312.93,121.14) -- (311.85,120.52) -- (310.77,121.14) -- (310.97,119.83) -- (310.1,118.91) -- (311.31,118.72) -- cycle ;
            	\draw (313,116) node [anchor=north west][inner sep=0.75pt]  [font=\fontsize{0.4em}{0.48em}\selectfont] [align=left] {29A-999.39};
            \end{tikzpicture} } \end{center}'''

                # Câu hỏi
                noidungcauhoi = (r'''Biển số xe ô tô ở thành phố Hà Nội quy định gồm 2 phần:\\
            - Phần thứ nhất là 29X, trong đó X là seri biển số sử dụng một trong $%s$ chữ cái.\\
            - Phần thứ hai là abc.de, trong đó $a,b,c,d,e \in \left\{0;1;2;3;4;5;6;7;8;9\right\}$. %s
            Một biển số xe được cho là "đẹp" khi phần thứ hai abc.de của nó có tổng $a+b+c+d+e$ là số có chữ số tận cùng bằng $%s$, và trong a,b,c,d,e có đúng 4 chữ số giống nhau. Tính số cách chọn đồng thời $%s$ biển số trong các biển số "đẹp" để đem bán đấu giá.'''
                                 %(n_letters, hinhve, k_end, choose_num))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


                # Nội dung lời giải
                loigiai = ('''Chọn X từ $%s$ chữ cái theo đề cho có $%s$ cách.\\\\
            Phần thứ hai là abc.de với $a,b,c,d,e \\in \\left\\{0;1;2;...;9\\right\\}$ thỏa mãn 2 điều kiện:\\\\
            - ĐK1: có đúng 4 chữ số giống nhau.\\\\
            - ĐK2: Tổng các chữ số có tận cùng là $%s$.\\\\
            Giả sử có 4 chữ số là $x$ và 1 chữ số là $y$, ta có $x,y \\in \\left\\{0;1;...;9\\right\\}, x \\neq y$.\\\\
            Tổng của 5 chữ số là $S = 4x+y$, ta lập luận S có chữ số tận cùng là $%s$, khi đó các cặp $\\left(x;y\\right)$ thỏa mãn là:
            $%s$\\\\
            $\\Rightarrow$ có 10 cặp $\\left(x;y\\right)$.\\\\
            Khi đã chọn 4 chữ số $x$ và 1 số $y$ thì ta sẽ hoán vị các số $x; x; x; x; y$ để tạo ra 1 biển số xe
            $\\Rightarrow$ có 5 biển số là $yxxxx; xyxxx; xxyxx; xxxyx; xxxxy$.\\\\
            Số biển số đẹp là $%s \\cdot 10 \\cdot 5 = %s$.\\\\
            Vậy số cách chọn $%s$ biển số đẹp là $C_{%s}^{%s} = %s$ (cách).'''
                           %(n_letters, n_letters,
                             k_end, k_end, pairs_str,
                             n_letters, total_plates,
                             choose_num, total_plates, choose_num, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content  

