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


def bt_dang63_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tỷ lệ k để tạo ra nhiều phiên bản bài toán khác nhau
                k = random.randint(1, 3)

                # Tính toán thể tích chính xác bằng math
                pi_val = math.pi
                sqrt2_val = math.sqrt(2)
                # Công thức thể tích tổng quát sau khi đã lấy nguyên hàm
                V_exact = (k**3) * ( (224 * pi_val / 15) + (4 * pi_val * sqrt2_val / 3) + (pi_val**2) )

                # Làm tròn đến hàng phần đơn vị
                kq3 = Decimal(float(V_exact)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(kq3)
                kq4 = int(kq3)

                #Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da= random.choice(du)

                # Tạo các phương án sai xung quanh kết quả đúng để gây nhiễu
                s = ['$%s$'%(latex(kq4+1)).replace('.',','),
                     '$%s$'%(latex(kq4+2)).replace('.',','),
                     '$%s$'%(latex(kq4+3)).replace('.',','),
                     '$%s$'%(latex(kq4-1)).replace('.',','),
                     '$%s$'%(latex(kq4-2)).replace('.',','),
                     '$%s$'%(latex(kq4-3)).replace('.',','),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Xử lý chuỗi hiển thị căn bậc 2 cho đẹp (ẩn số 1 nếu k=1)
                str_k_sqrt2 = "\\sqrt{2}" if k == 1 else "%s\\sqrt{2}" % latex(k)
                str_y_end = "%s + %s" % (latex(5*k), str_k_sqrt2)
                hinhve=r'''\begin{center} \scalebox{0.8}{ 
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_1ufzga8gb/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-26 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_4w5wv4i56}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            			rgb(37.5bp)=(0.55,0.34,0.16);
            			rgb(46.57143184116909bp)=(0.96,0.65,0.14);
            			rgb(62.5bp)=(0.55,0.34,0.16);
            			rgb(100bp)=(0.55,0.34,0.16)}
            		\tikzset {_ckuljv38d/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-9 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_twiu6a1zl}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            			rgb(37.5bp)=(0.55,0.34,0.16);
            			rgb(46.589290073939736bp)=(0.96,0.65,0.14);
            			rgb(62.5bp)=(0.55,0.34,0.16);
            			rgb(100bp)=(0.55,0.34,0.16)}
            		\tikzset {_mfd2gwwu3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            		\pgfdeclareradialshading{_79yxfl2kd}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(0.96,0.65,0.14);
            			rgb(12.303570338657924bp)=(0.96,0.65,0.14);
            			rgb(19.248886108398438bp)=(0.55,0.34,0.16);
            			rgb(23.356028965541295bp)=(0,0,0);
            			rgb(400bp)=(0,0,0)}
            		\tikzset{every picture/.style={line width=0.75pt}}  
            		\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (99.81,228.88) .. controls (99.81,215.58) and (137.85,204.8) .. (184.77,204.8) .. controls (231.7,204.8) and (269.73,215.58) .. (269.73,228.88) .. controls (269.73,242.17) and (231.7,252.95) .. (184.77,252.95) .. controls (137.85,252.95) and (99.81,242.17) .. (99.81,228.88) -- cycle ;
            		\path  [shading=_4w5wv4i56,_1ufzga8gb] (116.48,207.88) .. controls (136.48,197.88) and (200.4,191.47) .. (253.07,207.88) .. controls (257.07,209.47) and (267.73,210.13) .. (269.73,228.88) .. controls (261.07,267.73) and (108.4,265.07) .. (99.81,228.88) .. controls (98.4,218.13) and (111.07,207.47) .. (116.48,207.88) -- cycle ; 
            		\draw   (116.48,207.88) .. controls (136.48,197.88) and (200.4,191.47) .. (253.07,207.88) .. controls (257.07,209.47) and (267.73,210.13) .. (269.73,228.88) .. controls (261.07,267.73) and (108.4,265.07) .. (99.81,228.88) .. controls (98.4,218.13) and (111.07,207.47) .. (116.48,207.88) -- cycle ; 
            		\path  [shading=_twiu6a1zl,_ckuljv38d] (159.73,103.07) .. controls (171.73,113.73) and (199.07,114.4) .. (210.4,104.4) .. controls (211.73,167.07) and (225.73,212.4) .. (253.07,207.88) .. controls (268.4,243.73) and (98.4,240.4) .. (116.48,207.88) .. controls (142.4,211.07) and (159.47,164.87) .. (159.73,103.07) -- cycle ; 
            		\draw   (159.73,103.07) .. controls (171.73,113.73) and (199.07,114.4) .. (210.4,104.4) .. controls (211.73,167.07) and (225.73,212.4) .. (253.07,207.88) .. controls (268.4,243.73) and (98.4,240.4) .. (116.48,207.88) .. controls (142.4,211.07) and (159.47,164.87) .. (159.73,103.07) -- cycle ;
            		\path  [shading=_79yxfl2kd,_mfd2gwwu3] (147.29,81.62) .. controls (147.29,60.55) and (164.37,43.47) .. (185.44,43.47) .. controls (206.51,43.47) and (223.59,60.55) .. (223.59,81.62) .. controls (223.59,102.69) and (206.51,119.77) .. (185.44,119.77) .. controls (164.37,119.77) and (147.29,102.69) .. (147.29,81.62) -- cycle ;
            		\draw   (147.29,81.62) .. controls (147.29,60.55) and (164.37,43.47) .. (185.44,43.47) .. controls (206.51,43.47) and (223.59,60.55) .. (223.59,81.62) .. controls (223.59,102.69) and (206.51,119.77) .. (185.44,119.77) .. controls (164.37,119.77) and (147.29,102.69) .. (147.29,81.62) -- cycle ; 
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (158.67,71.2) .. controls (158.67,66.12) and (162.49,62) .. (167.2,62) .. controls (171.91,62) and (175.73,66.12) .. (175.73,71.2) .. controls (175.73,76.28) and (171.91,80.4) .. (167.2,80.4) .. controls (162.49,80.4) and (158.67,76.28) .. (158.67,71.2) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (165.33,122) .. controls (177.07,130.4) and (175.73,121.07) .. (179.73,124.4) .. controls (177.73,155.73) and (184.4,209.07) .. (168.4,231.07) .. controls (155.07,232.4) and (139.07,229.73) .. (129.73,223.07) .. controls (161.07,183.07) and (165.73,147.73) .. (165.33,122) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (209.73,116.4) .. controls (199.41,124.8) and (197.92,118.4) .. (194.4,121.73) .. controls (193.07,132.4) and (190.99,211.07) .. (205.07,233.07) .. controls (216.8,234.4) and (249.73,224.4) .. (253.73,213.07) .. controls (219.07,203.73) and (209.38,142.13) .. (209.73,116.4) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (165.33,122) .. controls (177.07,130.4) and (166.4,120.4) .. (170.4,123.73) .. controls (168.4,155.07) and (166.4,195.73) .. (144.4,229.73) .. controls (135.73,225.07) and (141.07,227.73) .. (129.73,223.07) .. controls (161.07,185.07) and (165.73,147.73) .. (165.33,122) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (209.73,116.4) .. controls (199.41,124.8) and (207.25,119.07) .. (203.73,122.4) .. controls (202.4,133.07) and (217.65,206.4) .. (231.73,228.4) .. controls (244.4,225.73) and (247.07,224.4) .. (253.73,213.07) .. controls (219.07,203.73) and (209.38,142.13) .. (209.73,116.4) -- cycle ;
            		\draw  [draw opacity=0][line width=1]  (349.59,254.53) .. controls (349.51,253.86) and (349.47,253.18) .. (349.47,252.49) .. controls (349.47,241.02) and (360.07,231.73) .. (373.13,231.73) .. controls (373.35,231.73) and (373.56,231.73) .. (373.78,231.73) -- (373.13,252.49) -- cycle ; \draw  [line width=1]  (349.59,254.53) .. controls (349.51,253.86) and (349.47,253.18) .. (349.47,252.49) .. controls (349.47,241.02) and (360.07,231.73) .. (373.13,231.73) .. controls (373.35,231.73) and (373.56,231.73) .. (373.78,231.73) ;  
            		\draw  [draw opacity=0][line width=1]  (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (496.71,231.73) and (507.3,241.14) .. (507.3,252.76) .. controls (507.3,252.94) and (507.3,253.11) .. (507.29,253.29) -- (483.64,252.76) -- cycle ; \draw  [line width=1]  (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (496.71,231.73) and (507.3,241.14) .. (507.3,252.76) .. controls (507.3,252.94) and (507.3,253.11) .. (507.29,253.29) ;  
            		\draw [line width=1]    (373.13,231.73) .. controls (396.4,232.13) and (403.47,134.2) .. (404.4,108.4) ;
            		\draw [line width=1]    (483.64,231.73) .. controls (457.86,232.13) and (453.43,134.04) .. (452.39,108.57) ;
            		\draw  [draw opacity=0][line width=1]  (404.74,109.29) .. controls (395.35,102.2) and (389.29,90.95) .. (389.29,78.29) .. controls (389.29,56.85) and (406.67,39.47) .. (428.11,39.47) .. controls (449.54,39.47) and (466.92,56.85) .. (466.92,78.29) .. controls (466.92,90.53) and (461.25,101.45) .. (452.39,108.57) -- (428.11,78.29) -- cycle ; \draw  [line width=1]  (404.74,109.29) .. controls (395.35,102.2) and (389.29,90.95) .. (389.29,78.29) .. controls (389.29,56.85) and (406.67,39.47) .. (428.11,39.47) .. controls (449.54,39.47) and (466.92,56.85) .. (466.92,78.29) .. controls (466.92,90.53) and (461.25,101.45) .. (452.39,108.57) ;  
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (488.63,231.77) -- (514.4,231.77) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (404.74,109.07) -- (513.73,109.07) ;
            		\draw [line width=1]    (349.69,253.36) -- (507.29,253.29) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (513.73,108.57) -- (513.73,252.4) ;
            		\draw (410,81.33) node [anchor=north west][inner sep=0.75pt]    {$%s$cm};
            		\draw (522,149.67) node [anchor=north west][inner sep=0.75pt]    {$%s$cm};
            		\draw (518.67,225.67) node [anchor=north west][inner sep=0.75pt]    {$%s$cm};
            		\draw (411.33,254) node [anchor=north west][inner sep=0.75pt]    {$%s$cm};
            		\draw (452.39,111) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (481.33,218) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (386.67,108) node [anchor=north west][inner sep=0.75pt]    {$F$};
            		\draw (363.33,218) node [anchor=north west][inner sep=0.75pt]    {$E$};
            	\end{tikzpicture} }
            \end{center}'''%(latex(2*k),latex(3*k),latex(k),latex(6*k))
                # Câu hỏi
                noidungcauhoi = (r'''Mô hình của quân tốt trong bàn cờ vua là một khối tròn xoay với mặt cắt qua trục như sau: Đầu của quân cờ là một phần của hình cầu có bán kính bằng $%s$ (cm); đường cong $AB$ và $EF$ là một phần của parabol đỉnh $B$ và đỉnh $E$; $DE$ và $BC$ là một góc phần tư của đường tròn có bán kính $%s$ (cm). Biết rằng cổ quân cờ có đường kính bằng $%s$ cm, khoảng cách từ đỉnh $B$ xuống mặt đáy là $%s$ cm, khoảng cách từ $A$ xuống mặt đáy là $%s$ cm, đường kính mặt đáy là $%s$ cm. %s Thể tích của mô hình quân tốt (đơn vị cm$^3$ bằng bao nhiêu? (Kết quả làm tròn đến hàng đơn vị).'''
                                 %(str_k_sqrt2, latex(k), latex(2*k), latex(k), latex(4*k), latex(6*k),hinhve
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center} \\scalebox{0.8}{ 
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw  [draw opacity=0][line width=1]  (349.59,254.53) .. controls (349.51,253.86) and (349.47,253.18) .. (349.47,252.49) .. controls (349.47,241.02) and (360.07,231.73) .. (373.13,231.73) .. controls (373.35,231.73) and (373.56,231.73) .. (373.78,231.73) -- (373.13,252.49) -- cycle ; \\draw  [line width=1]  (349.59,254.53) .. controls (349.51,253.86) and (349.47,253.18) .. (349.47,252.49) .. controls (349.47,241.02) and (360.07,231.73) .. (373.13,231.73) .. controls (373.35,231.73) and (373.56,231.73) .. (373.78,231.73) ;  
                		\\draw  [draw opacity=0][line width=1]  (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (496.71,231.73) and (507.3,241.14) .. (507.3,252.76) .. controls (507.3,252.94) and (507.3,253.11) .. (507.29,253.29) -- (483.64,252.76) -- cycle ; \\draw  [line width=1]  (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (483.64,231.73) and (483.64,231.73) .. (483.64,231.73) .. controls (496.71,231.73) and (507.3,241.14) .. (507.3,252.76) .. controls (507.3,252.94) and (507.3,253.11) .. (507.29,253.29) ;  
                		\\draw [line width=1]    (373.13,231.73) .. controls (396.4,232.13) and (403.47,134.2) .. (404.4,108.4) ;
                		\\draw [line width=1]    (483.64,231.73) .. controls (457.86,232.13) and (453.43,134.04) .. (452.39,108.57) ;
                		\\draw  [draw opacity=0][line width=1]  (404.74,109.29) .. controls (395.35,102.2) and (389.29,90.95) .. (389.29,78.29) .. controls (389.29,56.85) and (406.67,39.47) .. (428.11,39.47) .. controls (449.54,39.47) and (466.92,56.85) .. (466.92,78.29) .. controls (466.92,90.53) and (461.25,101.45) .. (452.39,108.57) -- (428.11,78.29) -- cycle ; \\draw  [line width=1]  (404.74,109.29) .. controls (395.35,102.2) and (389.29,90.95) .. (389.29,78.29) .. controls (389.29,56.85) and (406.67,39.47) .. (428.11,39.47) .. controls (449.54,39.47) and (466.92,56.85) .. (466.92,78.29) .. controls (466.92,90.53) and (461.25,101.45) .. (452.39,108.57) ;  
                		\\draw [line width=1]    (349.69,253.36) -- (507.29,253.29) ;
                		\\draw [line width=1]    (318.4,253.07) -- (549.73,253.07) ;
                		\\draw [shift={(553.73,253.07)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw [line width=1]    (428.73,273.07) -- (428.73,19.07) ;
                		\\draw [shift={(428.73,15.07)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw (452.39,108.57) node [anchor=north west][inner sep=0.75pt]    {$A$};
                		\\draw (481.33,211) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (386.67,102.33) node [anchor=north west][inner sep=0.75pt]    {$F$};
                		\\draw (363.33,207.67) node [anchor=north west][inner sep=0.75pt]    {$E$};
                		\\draw (535.33,259) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (407.33,15) node [anchor=north west][inner sep=0.75pt]    {$y$};
                		\\draw (496,259) node [anchor=north west][inner sep=0.75pt]    {$C$};
                		\\draw (405,259) node [anchor=north west][inner sep=0.75pt]    {$O$};
                	\\end{tikzpicture} }
                \\end{center}
                Chọn hệ trục tọa độ $Oxy$ như hình vẽ, với $O$ là trung điểm của mặt đáy.\\\\
                Các điểm có tọa độ: $C(%s; 0)$, $B(%s; %s)$, $A(%s; %s)$.\\\\
                Đường tròn chứa cung $BC$ có tâm $I(%s; 0)$, bán kính $R_1 = %s$. \\\\
                    Phương trình: $(x - %s)^2 + y^2 = %s \\Rightarrow x = %s + \\sqrt{%s - y^2}$ (với $0 \\le y \\le %s$).\\\\
                Parabol chứa cung $AB$ có đỉnh $B(%s; %s)$ nên có dạng $x = a(y - %s)^2 + %s$. \\\\
                    Đi qua $A(%s; %s) \\Rightarrow %s = a(%s - %s)^2 + %s \\Rightarrow a = -\\frac{1}{%s}$. \\\\
                        Phương trình: $x = %s - \\frac{1}{%s}(y - %s)^2$ (với $%s \\le y \\le %s$).\\\\
                Đường tròn chứa cung $AF$ có bán kính $R_2 = %s$. Tâm $J(0; y_J)$ trên trục $Oy$. \\\\
                    Đi qua $A(%s; %s)$ nên $%s + (y_J - %s)^2 = %s \\Rightarrow y_J = %s$. \\\\
                        Phương trình: $x^2 + (y - %s)^2 = %s \\Rightarrow x = \\sqrt{%s - (y - %s)^2}$. \\\\
                            Cung $AF$ giới hạn từ $y = %s$ đến $y = %s$.\\\\
                Thể tích $V = V_1 + V_2 + V_3$ với:\\\\
                $V_1 = \\pi \\int_{0}^{%s} \\left( %s + \\sqrt{%s - y^2} \\right)^2 \\mathrm{d}y = %s \\left( \\frac{14\\pi}{3} + \\pi^2 \\right)$\\\\
                $V_2 = \\pi \\int_{%s}^{%s} \\left( %s - \\frac{1}{%s}(y - %s)^2 \\right)^2 \\mathrm{d}y = %s \\left( \\frac{43\\pi}{5} \\right)$\\\\
                $V_3 = \\pi \\int_{%s}^{%s} \\left( %s - (y - %s)^2 \\right) \\mathrm{d}y = %s \\left( \\frac{5\\pi}{3} + \\frac{4\\pi\\sqrt{2}}{3} \\right)$\\\\
                Vậy $V = %s \\left( \\frac{224\\pi}{15} + \\frac{4\\pi\\sqrt{2}}{3} + \\pi^2 \\right) \\approx %s$ cm$^3$.'''

                         %(latex(3*k), latex(2*k), latex(k), latex(k), latex(4*k), # Tọa độ điểm
                           latex(2*k), latex(k), latex(2*k), latex(k**2), latex(2*k), latex(k**2), latex(k), # Cung BC
                           latex(2*k), latex(k), latex(k), latex(2*k), latex(k), latex(4*k), latex(k), latex(4*k), latex(k), latex(2*k), latex(9*k), latex(2*k), latex(9*k), latex(k), latex(k), latex(4*k), # Parabol AB
                           str_k_sqrt2, latex(k), latex(4*k), latex(k**2), latex(4*k), latex(2*k**2), latex(5*k), latex(5*k), latex(2*k**2), latex(2*k**2), latex(5*k), latex(4*k), str_y_end, # Đường tròn AF
                           latex(k), latex(2*k), latex(k**2), latex(k**3), # V1
                           latex(k), latex(4*k), latex(2*k), latex(9*k), latex(k), latex(k**3), # V2
                           latex(4*k), str_y_end, latex(2*k**2), latex(5*k), latex(k**3), # V3
                           latex(k**3), latex(kq) # Tổng thể tích
                         ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

