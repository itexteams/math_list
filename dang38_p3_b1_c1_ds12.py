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


def bt_dang38_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số p (chọn số chẵn để kết quả là số nguyên)
                p = random.choice([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

                # Đáp án đúng (K = 1/2)
                kq = p // 2

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Các phương án nhiễu
                s = ['$%s$'%(kq + 1),
                     '$%s$'%(kq + 2),
                     '$%s$'%(kq + 3),
                     '$%s$'%(kq - 1),
                     '$%s$'%(kq - 2),
                     '$%s$'%(kq + 4),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                cau_hoi_cuoi = 'Giá trị của $%sK$ bằng bao nhiêu?' % p

                noidungcauhoi = ('''\\immini{Một bồn hình trụ cao $h$ chứa nước. Theo định luật Torricelli, vận tốc tia nước chảy qua lỗ ở độ sâu $x$ so với mặt nước là $V = \\sqrt{2gx}$. Người ta cho rằng tầm xa $R$ (feet) của tia nước được cho bởi $R = 2\\sqrt{x(h-x)}$. Biết lỗ phun nên đặt ở độ sâu $x = K.h, (K \\in \\mathbb{R})$ so với mặt nước thì tầm xa $R$ đạt cực đại. %s}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 	\\tikzset {_v9tyk12ii/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                                 	\\pgfdeclarehorizontalshading{_32595orbk}{150bp}{rgb(0bp)=(0.31,0.89,0.76);
                                 		rgb(37.66071319580078bp)=(0.31,0.89,0.76);
                                 		rgb(46.12388610839844bp)=(1,1,1);
                                 		rgb(62.5bp)=(0.31,0.89,0.76);
                                 		rgb(100bp)=(0.31,0.89,0.76)}
                                 	\\tikzset{every picture/.style={line width=0.75pt}} 
                                 	\\path  [shading=_32595orbk,_v9tyk12ii] (345,60.4) -- (345,218.4) .. controls (345,228.34) and (324.41,236.4) .. (299,236.4) .. controls (273.59,236.4) and (253,228.34) .. (253,218.4) -- (253,60.4) .. controls (253,50.46) and (273.59,42.4) .. (299,42.4) .. controls (324.41,42.4) and (345,50.46) .. (345,60.4) .. controls (345,70.34) and (324.41,78.4) .. (299,78.4) .. controls (273.59,78.4) and (253,70.34) .. (253,60.4) ; 
                                 	\\draw  [color={rgb, 255:red, 89; green, 129; blue, 120 }  ,draw opacity=1 ] (345,60.4) -- (345,218.4) .. controls (345,228.34) and (324.41,236.4) .. (299,236.4) .. controls (273.59,236.4) and (253,228.34) .. (253,218.4) -- (253,60.4) .. controls (253,50.46) and (273.59,42.4) .. (299,42.4) .. controls (324.41,42.4) and (345,50.46) .. (345,60.4) .. controls (345,70.34) and (324.41,78.4) .. (299,78.4) .. controls (273.59,78.4) and (253,70.34) .. (253,60.4) ; 
                                 	\\draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (253,218.4) .. controls (253,218.4) and (253,218.4) .. (253,218.4) .. controls (253,208.46) and (273.59,200.4) .. (299,200.4) .. controls (324.41,200.4) and (345,208.46) .. (345,218.4) -- (299,218.4) -- cycle ; \\draw  [color={rgb, 255:red, 104; green, 136; blue, 174 }  ,draw opacity=1 ][dash pattern={on 4.5pt off 4.5pt}] (253,218.4) .. controls (253,218.4) and (253,218.4) .. (253,218.4) .. controls (253,208.46) and (273.59,200.4) .. (299,200.4) .. controls (324.41,200.4) and (345,208.46) .. (345,218.4) ;  
                                 	\\draw  [draw opacity=0] (344.94,112.35) .. controls (343.67,121.85) and (323.59,129.4) .. (299,129.4) .. controls (273.59,129.4) and (253,121.34) .. (253,111.4) -- (299,111.4) -- cycle ; \\draw  [color={rgb, 255:red, 80; green, 227; blue, 194 }  ,draw opacity=1 ] (344.94,112.35) .. controls (343.67,121.85) and (323.59,129.4) .. (299,129.4) .. controls (273.59,129.4) and (253,121.34) .. (253,111.4) ;  
                                 	\\draw  [draw opacity=0] (344.94,161.35) .. controls (343.67,170.85) and (323.59,178.4) .. (299,178.4) .. controls (273.59,178.4) and (253,170.34) .. (253,160.4) -- (299,160.4) -- cycle ; \\draw  [color={rgb, 255:red, 80; green, 227; blue, 194 }  ,draw opacity=1 ] (344.94,161.35) .. controls (343.67,170.85) and (323.59,178.4) .. (299,178.4) .. controls (273.59,178.4) and (253,170.34) .. (253,160.4) ;  
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 56; green, 211; blue, 176 }  ,fill opacity=1 ] (253,60.4) .. controls (253,50.46) and (273.59,42.4) .. (299,42.4) .. controls (324.41,42.4) and (345,50.46) .. (345,60.4) .. controls (345,70.34) and (324.41,78.4) .. (299,78.4) .. controls (273.59,78.4) and (253,70.34) .. (253,60.4) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=0.37 ] (253,218.4) .. controls (253,208.46) and (273.59,200.4) .. (299,200.4) .. controls (324.41,200.4) and (345,208.46) .. (345,218.4) .. controls (345,228.34) and (324.41,236.4) .. (299,236.4) .. controls (273.59,236.4) and (253,228.34) .. (253,218.4) -- cycle ;
                                 	\\draw    (345,60.4) -- (380,60.4) ;
                                 	\\draw    (218,60.4) -- (253,60.4) ;
                                 	\\draw    (218,218.4) -- (253,218.4) ;
                                 	\\draw    (345,218.4) -- (401,218.4) ;
                                 	\\draw    (345.44,99.35) -- (380.44,99.35) ;
                                 	\\draw    (371,64) -- (371,95.4) ;
                                 	\\draw [shift={(371,98.4)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw [shift={(371,61)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw    (230.5,64) -- (230.5,214.9) ;
                                 	\\draw [shift={(230.5,217.9)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw [shift={(230.5,61)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw    (345,218.4) -- (345,236.4) ;
                                 	\\draw    (380,218.4) -- (380,236.4) ;
                                 	\\draw    (377,230.4) -- (348,230.4) ;
                                 	\\draw [shift={(345,230.4)}, rotate = 360] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw [shift={(380,230.4)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
                                 	\\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ]   (345.44,99.35) .. controls (375.5,102.4) and (386.5,176.4) .. (389,217.9) ;
                                 	\\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ]   (345.44,99.35) .. controls (375.5,102.4) and (389,176.9) .. (391.5,218.4) ;
                                 	\\draw (215.5,125) node [anchor=north west][inner sep=0.75pt]    {$h$};
                                 	\\draw (375.5,77) node [anchor=north west][inner sep=0.75pt]    {$x$};
                                 	\\draw (353.5,238) node [anchor=north west][inner sep=0.75pt]    {$R$};
                                 \\end{tikzpicture}}''' 
                                 % cau_hoi_cuoi)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta có tầm xa của tia nước là $R(x) = 2\\sqrt{x(h-x)}$ với $0 < x < h$. \\\\
                         Để $R$ đạt cực đại thì biểu thức trong căn phải lớn nhất, xét hàm số $f(x) = x(h-x) = hx - x^2$ trên khoảng $(0; h)$. \\\\
                         Ta có đạo hàm $f'(x) = h - 2x$. \\\\
                         Cho $f'(x) = 0 \\Leftrightarrow h - 2x = 0 \\Leftrightarrow x = \\frac{1}{2}h$. \\\\
                         Ta thấy $f'(x)$ đổi dấu từ dương sang âm khi qua điểm $x = \\frac{1}{2}h$ nên hàm số đạt giá trị lớn nhất tại $x = \\frac{1}{2}h$. \\\\
                         Vậy tầm xa $R$ đạt cực đại khi $x = \\frac{1}{2}h$. \\\\
                         Đồng nhất với giả thiết ta suy ra $K = \\frac{1}{2}$. \\\\
                         Giá trị cần tìm là $%s K = %s \\cdot \\frac{1}{2} = %s$.'''
                         %(latex(p), latex(p), latex(kq)
                         ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content  

