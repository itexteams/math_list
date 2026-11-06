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


def bt_dang54_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random bán kính R từ 15 đến 25, đường kính D = 2*R
                R = random.randint(15, 25)
                D = 2 * R
                # Random chiều sâu h (chọn số chẵn để đảm bảo a là số nguyên)
                h = random.choice([20, 24, 30, 36, 40, 50])

                # Tính toán đáp án đúng: a = (R^2 * h) / 2
                a = int((R**2 * h) / 2)

                # Tính các thông số hệ số parabol y = cx^2 => c = h / R^2, nghịch đảo 1/c = R^2 / h
                c_val = Rational(h, R**2)
                c_inv = Rational(R**2, h)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(a)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai)
                das1_val = R**2 * h
                das2_val = int((R**2 * h) / 3) if (R**2 * h) % 3 == 0 else a + 1200
                das3_val = int((D**2 * h) / 2)

                s = ['$%s$' % (das1_val),
                     '$%s$' % (das2_val),
                     '$%s$' % (das3_val),
                     '$%s$' % (a + 1000),
                     '$%s$' % (a - 1000),
                     '$%s$' % (a + 500),
                     '$%s$' % (a - 500)]

                # Loại bỏ các đáp án trùng với đáp án đúng để đảm bảo phương án sai khác phương án đúng
                s_unique = []
                for item in s:
                    if item not in s_unique and item != da:
                        s_unique.append(item)

                das1 = s_unique[0]
                das2 = s_unique[1]
                das3 = s_unique[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_fq2a7ll7t/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_cp10a8zmc}{150bp}{rgb(0bp)=(0.4,0.42,0.42);
            		rgb(37.5bp)=(0.4,0.42,0.42);
            		rgb(50bp)=(1,1,1);
            		rgb(62.5bp)=(0.36,0.38,0.38);
            		rgb(100bp)=(0.36,0.38,0.38)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [fill={rgb, 255:red, 195; green, 205; blue, 200 }  ,fill opacity=1 ] (310.6,185.9) -- (318.6,168) -- (390.1,168) -- (398.1,185.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (339.67,186.61) .. controls (339.66,186.54) and (339.66,186.47) .. (339.66,186.4) .. controls (339.66,178.94) and (345.76,172.9) .. (353.28,172.9) .. controls (360.79,172.9) and (366.89,178.94) .. (366.89,186.4) .. controls (366.89,186.48) and (366.89,186.55) .. (366.88,186.63) -- (353.28,186.4) -- cycle ; \draw   (339.67,186.61) .. controls (339.66,186.54) and (339.66,186.47) .. (339.66,186.4) .. controls (339.66,178.94) and (345.76,172.9) .. (353.28,172.9) .. controls (360.79,172.9) and (366.89,178.94) .. (366.89,186.4) .. controls (366.89,186.48) and (366.89,186.55) .. (366.88,186.63) ;  
            	\draw  [fill={rgb, 255:red, 201; green, 211; blue, 209 }  ,fill opacity=1 ] (279.5,61) .. controls (300.1,34.4) and (429.1,38.9) .. (429.1,60.9) .. controls (421.6,114.9) and (349.5,91) .. (369.5,121) .. controls (389.5,151) and (334.1,164.4) .. (314.1,134.4) .. controls (294.1,104.4) and (293.6,105.9) .. (279.5,61) -- cycle ;
            	\path  [shading=_cp10a8zmc,_fq2a7ll7t] (289.11,60.5) .. controls (301.71,36.9) and (423.71,44.4) .. (419.71,60.9) .. controls (424.21,95.9) and (406.71,107.4) .. (405.71,133.9) .. controls (396.21,174.9) and (328.21,173.4) .. (308.21,143.4) .. controls (288.21,113.4) and (286.71,85.4) .. (289.11,60.5) -- cycle ;  
            	\draw   (289.11,60.5) .. controls (301.71,36.9) and (423.71,44.4) .. (419.71,60.9) .. controls (424.21,95.9) and (406.71,107.4) .. (405.71,133.9) .. controls (396.21,174.9) and (328.21,173.4) .. (308.21,143.4) .. controls (288.21,113.4) and (286.71,85.4) .. (289.11,60.5) -- cycle ;  
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (291,68.5) .. controls (318.6,51.9) and (389.1,55.4) .. (416.6,64.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (292,62.5) .. controls (319.6,45.9) and (390.1,49.4) .. (417.6,58.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (292,74) .. controls (319.6,57.4) and (390.1,60.9) .. (417.6,70.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (294,80) .. controls (321.6,63.4) and (392.1,66.9) .. (419.6,76.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (296.5,85.5) .. controls (324.1,68.9) and (394.6,72.4) .. (422.1,81.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (297.1,91.4) .. controls (324.7,74.8) and (390.6,78.4) .. (418.1,87.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (294.5,97.5) .. controls (322.1,80.9) and (392.6,84.4) .. (420.1,93.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (295,103.5) .. controls (322.6,86.9) and (393.1,90.4) .. (420.6,99.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (301.1,106.4) .. controls (330.1,93.4) and (378.6,96.4) .. (409.6,102.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (300.1,112.4) .. controls (329.1,99.4) and (377.6,102.4) .. (408.6,108.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (300.6,117.9) .. controls (329.6,104.9) and (378.1,107.9) .. (409.1,114.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (301.1,123.4) .. controls (330.1,110.4) and (378.6,113.4) .. (409.6,119.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (305.1,127.9) .. controls (334.1,114.9) and (382.6,117.9) .. (413.6,124.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (312.1,130.4) .. controls (342.1,120.4) and (367.6,121.4) .. (399.6,126.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (314.1,134.4) .. controls (344.1,124.4) and (368.6,126.4) .. (400.6,131.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (312.6,139.4) .. controls (342.6,129.4) and (367.1,131.4) .. (399.1,136.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (312.1,143.4) .. controls (342.1,133.4) and (366.6,135.4) .. (398.6,140.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (309.6,146.9) .. controls (339.6,136.9) and (364.1,138.9) .. (396.1,143.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (310.6,150.9) .. controls (340.6,140.9) and (365.1,142.9) .. (397.1,147.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (312.6,154.4) .. controls (342.6,144.4) and (367.1,146.4) .. (399.1,151.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (315.1,158.4) .. controls (345.1,148.4) and (369.6,150.4) .. (401.6,155.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (316.1,161.9) .. controls (346.1,151.9) and (370.6,153.9) .. (402.6,158.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.36 ] (319.1,155.45) .. controls (319.1,148.52) and (334.77,142.9) .. (354.1,142.9) .. controls (373.43,142.9) and (389.1,148.52) .. (389.1,155.45) .. controls (389.1,162.38) and (373.43,168) .. (354.1,168) .. controls (334.77,168) and (319.1,162.38) .. (319.1,155.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.36 ] (315.6,145.7) .. controls (315.6,136.97) and (333.06,129.9) .. (354.6,129.9) .. controls (376.14,129.9) and (393.6,136.97) .. (393.6,145.7) .. controls (393.6,154.43) and (376.14,161.5) .. (354.6,161.5) .. controls (333.06,161.5) and (315.6,154.43) .. (315.6,145.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.36 ] (300.6,139.2) .. controls (300.6,126.88) and (324.78,116.9) .. (354.6,116.9) .. controls (384.42,116.9) and (408.6,126.88) .. (408.6,139.2) .. controls (408.6,151.52) and (384.42,161.5) .. (354.6,161.5) .. controls (324.78,161.5) and (300.6,151.52) .. (300.6,139.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 215; green, 222; blue, 220 }  ,fill opacity=1 ] (279.5,61) .. controls (281.71,60.99) and (284.99,60.81) .. (289.11,60.5) .. controls (339.6,212.9) and (383.1,170.9) .. (419.14,60.22) .. controls (423.13,60.44) and (426.51,60.66) .. (429.1,60.9) .. controls (431.1,80.9) and (425.1,138.9) .. (391.1,169.4) .. controls (359.1,169.4) and (365.1,170.9) .. (317.6,169.9) .. controls (295.1,150.9) and (275.1,93.4) .. (279.5,61) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một chiếc cối đá có lòng cối là một paraboloid tròn xoay (có mặt cắt qua trục là một parabol như hình bên), với miệng cối là đường tròn có đường kính $%s$ cm và chiều sâu lòng cối là $%s$ cm. Biết rằng thể tích của lòng cối bằng $a\pi$ $\left(\text{cm}^3\right)$, giá trị $a$ bằng bao nhiêu?}{%s}'''
                                 %(latex(D), latex(h),hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Bán kính của miệng cối là $R = \\frac{%s}{2} = %s$ cm. \\\\
                Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O$ trùng với đỉnh của parabol, trục $Oy$ trùng với trục đối xứng của parabol (hướng lên trên). \\\\
                Khi đó, mặt cắt qua trục là một parabol có phương trình dạng $y = cx^2$. \\\\
                Vì parabol đi qua điểm thuộc miệng cối có tọa độ $\\left(%s; %s\\right)$ nên ta có: \\\\
                $%s = c \\cdot %s^2 \\Rightarrow c = %s$. \\\\
                Do đó, phương trình parabol là $y = %s x^2 \\Rightarrow x^2 = %s y$. \\\\
                Thể tích của lòng cối là thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi parabol và đường thẳng $y = %s$ quanh trục $Oy$: \\\\
                $V = \\pi \\int_0^{%s} x^2 \\mathrm{d}y = \\pi \\int_0^{%s} \\left(%s y\\right) \\mathrm{d}y = \\pi \\cdot %s \\left[\\frac{y^2}{2}\\right]_0^{%s} = \\pi \\cdot %s \\cdot \\frac{%s^2}{2} = %s\\pi$ $\\left(\\text{cm}^3\\right)$. \\\\
                Vậy $a = %s$.'''
                %(latex(D), latex(R),
                  latex(R), latex(h),
                  latex(h), latex(R), latex(c_val),
                  latex(c_val), latex(c_inv),
                  latex(h),
                  latex(h), latex(h), latex(c_inv), latex(c_inv), latex(h), latex(c_inv), latex(h), latex(a),
                  latex(a)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(a))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

