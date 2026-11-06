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


def bt_dang16_p3_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random khoảng cách L (m) và góc dốc alpha (độ)
                L = random.choice([200, 300, 400, 500, 600, 800])
                alpha = random.choice([8, 9, 10, 11, 12, 15])

                # Tính toán các đại lượng phụ
                L2 = int(L / 2) # Nửa khoảng cách

                # Tính chiều cao h = L * tan(alpha) / 4
                h_exact = (L * math.tan(math.radians(alpha))) / 4

                # Làm tròn đến 1 chữ số thập phân
                kq_decimal = Decimal(float(h_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_decimal).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai lầm thường gặp: quên chia 4, chia 2, hoặc tính sai)
                s = [
                    '$%s$' % str(Decimal(float((L * math.tan(math.radians(alpha))) / 2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(h_exact * 2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(h_exact + 1.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(h_exact - 1.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(h_exact + 2.4)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(h_exact - 2.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Đảm bảo phương án sai không trùng đáp án đúng và không trùng nhau
                while das1 == da or das2 == da or das3 == da or das1 == das2 or das1 == das3 or das2 == das3:
                    s = [
                        '$%s$' % str(Decimal(float(h_exact + random.uniform(3, 7))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                        '$%s$' % str(Decimal(float(h_exact - random.uniform(3, 7))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                        '$%s$' % str(Decimal(float(h_exact * 1.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    ]
                    das1 = s[0]
                    das2 = s[1]
                    das3 = s[2]
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_5ikjkcyc5/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_7e52e6m6o}{150bp}{rgb(0bp)=(0.76,0.75,0.67);
            			rgb(37.5bp)=(0.76,0.75,0.67);
            			rgb(50bp)=(1,1,1);
            			rgb(62.5bp)=(0.52,0.51,0.45);
            			rgb(100bp)=(0.52,0.51,0.45)}
            		\tikzset {_qpeyeq1z8/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_mxdx5spq2}{150bp}{rgb(0bp)=(0.67,0.66,0.6);
            			rgb(37.571427481515066bp)=(0.67,0.66,0.6);
            			rgb(50bp)=(1,1,1);
            			rgb(62.5bp)=(0.46,0.45,0.41);
            			rgb(100bp)=(0.46,0.45,0.41)}
            		\tikzset {_80lyqob0r/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_x50bpy320}{150bp}{rgb(0bp)=(0.39,0.38,0.36);
            			rgb(37.5bp)=(0.39,0.38,0.36);
            			rgb(50.071427481515066bp)=(1,1,1);
            			rgb(62.5bp)=(0.46,0.46,0.42);
            			rgb(100bp)=(0.46,0.46,0.42)}
            		\tikzset {_qeajvc9hx/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_3eh4nm3pj}{150bp}{rgb(0bp)=(0.39,0.38,0.36);
            			rgb(37.5bp)=(0.39,0.38,0.36);
            			rgb(50.071427481515066bp)=(1,1,1);
            			rgb(62.5bp)=(0.46,0.46,0.42);
            			rgb(100bp)=(0.46,0.46,0.42)}
            		\tikzset{every picture/.style={line width=0.75pt}}   
            		\draw  [line width=1]  (566.8,118.67) .. controls (400.09,44.18) and (233.38,44.18) .. (66.67,118.67) ;
            		\draw [line width=1]    (66.67,124.67) -- (566.8,124.67) ;
            		\draw  [line width=1]  (566.8,124.67) .. controls (400.09,50.18) and (233.38,50.18) .. (66.67,124.67) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (239,67.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (189.5,76.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (215,71.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (168.5,82.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (87.5,109.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (129,94.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (108,101.4) ;
            		\path  [shading=_7e52e6m6o,_5ikjkcyc5] (138,124.5) -- (147.3,26.9) -- (149.7,26.9) -- (159,124.5) -- cycle ; 
            		\draw  [line width=1]  (138,124.5) -- (147.3,26.9) -- (149.7,26.9) -- (159,124.5) -- cycle ; 
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (391,66.9) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (444.5,76.9) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (420,71.9) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (464,81.9) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (550,110.9) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (508.5,95.4) -- (484.5,53.4) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (526.5,101.9) -- (484.5,53.4) ;
            		\path  [shading=_mxdx5spq2,_qpeyeq1z8] (475.5,124.5) -- (484.8,26.9) -- (487.2,26.9) -- (496.5,124.5) -- cycle ; 
            		\draw  [line width=1]  (475.5,124.5) -- (484.8,26.9) -- (487.2,26.9) -- (496.5,124.5) -- cycle ; 
            		\path  [shading=_x50bpy320,_80lyqob0r] (128,124) -- (136.5,111.9) -- (161.5,111.9) -- (170,124) -- cycle ; 
            		\draw  [line width=1]  (128,124) -- (136.5,111.9) -- (161.5,111.9) -- (170,124) -- cycle ;
            		\path  [shading=_3eh4nm3pj,_qeajvc9hx] (465.5,124.5) -- (474,112.4) -- (499,112.4) -- (507.5,124.5) -- cycle ; 
            		\draw  [line width=1]  (465.5,124.5) -- (474,112.4) -- (499,112.4) -- (507.5,124.5) -- cycle ; 
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Người ta xây một cây cầu vượt giao thông hình parabol nối hai điểm có khoảng cách là $%s$ m. Độ dốc của mặt cầu không vượt quá $%s^\circ$ (độ dốc tại một điểm được xác định bởi góc giữa phương tiếp xúc với mặt cầu và phương ngang). %s Tính chiều cao giới hạn từ đỉnh cầu đến mặt đường (làm tròn kết quả đến chữ số thập phân thứ nhất).'''
                                 %(latex(L), latex(alpha),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O$ trùng với trung điểm của đoạn thẳng nối hai điểm chân cầu, trục $Ox$ nằm trên mặt đường. \\\\
                    \\begin{center}
                    		\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                    		\\tikzset {_8y4lxgibc/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                    		\\pgfdeclarehorizontalshading{_gv8bdfa2v}{150bp}{rgb(0bp)=(0.76,0.75,0.67);
                    			rgb(37.5bp)=(0.76,0.75,0.67);
                    			rgb(50bp)=(1,1,1);
                    			rgb(62.5bp)=(0.52,0.51,0.45);
                    			rgb(100bp)=(0.52,0.51,0.45)}
                    		\\tikzset {_e77jzkwsz/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                    		\\pgfdeclarehorizontalshading{_d4kpivyug}{150bp}{rgb(0bp)=(0.67,0.66,0.6);
                    			rgb(37.571427481515066bp)=(0.67,0.66,0.6);
                    			rgb(50bp)=(1,1,1);
                    			rgb(62.5bp)=(0.46,0.45,0.41);
                    			rgb(100bp)=(0.46,0.45,0.41)}
                    		\\tikzset {_aab3dafly/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                    		\\pgfdeclarehorizontalshading{_z0qgumoz2}{150bp}{rgb(0bp)=(0.39,0.38,0.36);
                    			rgb(37.5bp)=(0.39,0.38,0.36);
                    			rgb(50.071427481515066bp)=(1,1,1);
                    			rgb(62.5bp)=(0.46,0.46,0.42);
                    			rgb(100bp)=(0.46,0.46,0.42)}
                    		\\tikzset {_78gs8ngpq/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                    		\\pgfdeclarehorizontalshading{_4454bk33h}{150bp}{rgb(0bp)=(0.39,0.38,0.36);
                    			rgb(37.5bp)=(0.39,0.38,0.36);
                    			rgb(50.071427481515066bp)=(1,1,1);
                    			rgb(62.5bp)=(0.46,0.46,0.42);
                    			rgb(100bp)=(0.46,0.46,0.42)}
                    		\\tikzset{every picture/.style={line width=0.75pt}} 
                    		\\draw  [line width=1]  (566.8,118.67) .. controls (400.09,44.18) and (233.38,44.18) .. (66.67,118.67) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (66.67,124.67) -- (566.8,124.67) ;
                    		\\draw  [line width=1]  (566.8,124.67) .. controls (400.09,50.18) and (233.38,50.18) .. (66.67,124.67) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (239,67.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (189.5,76.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (215,71.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (168.5,82.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (87.5,109.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (129,94.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (147.75,41.4) -- (108,101.4) ;
                    		\\path  [shading=_gv8bdfa2v,_8y4lxgibc] (138,124.5) -- (147.3,26.9) -- (149.7,26.9) -- (159,124.5) -- cycle ; 
                    		\\draw  [line width=1]  (138,124.5) -- (147.3,26.9) -- (149.7,26.9) -- (159,124.5) -- cycle ; 
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (391,66.9) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (444.5,76.9) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (420,71.9) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (464,81.9) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (550,110.9) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (508.5,95.4) -- (484.5,53.4) ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (526.5,101.9) -- (484.5,53.4) ;
                    		\\path  [shading=_d4kpivyug,_e77jzkwsz] (475.5,124.5) -- (484.8,26.9) -- (487.2,26.9) -- (496.5,124.5) -- cycle ; 
                    		\\draw  [line width=1]  (475.5,124.5) -- (484.8,26.9) -- (487.2,26.9) -- (496.5,124.5) -- cycle ; 
                    		\\path  [shading=_z0qgumoz2,_aab3dafly] (128,124) -- (136.5,111.9) -- (161.5,111.9) -- (170,124) -- cycle ; 
                    		\\draw  [line width=1]  (128,124) -- (136.5,111.9) -- (161.5,111.9) -- (170,124) -- cycle ; 
                    		\\path  [shading=_4454bk33h,_78gs8ngpq] (465.5,124.5) -- (474,112.4) -- (499,112.4) -- (507.5,124.5) -- cycle ; 
                    		\\draw  [line width=1]  (465.5,124.5) -- (474,112.4) -- (499,112.4) -- (507.5,124.5) -- cycle ; 
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (507.5,124.5) -- (592.8,125.09) ;
                    		\\draw [shift={(596.8,125.12)}, rotate = 180.4] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (315.5,146.1) -- (313.66,31.52) ;
                    		\\draw [shift={(313.6,27.52)}, rotate = 89.08] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                    		\\draw (294.4,129) node [anchor=north west][inner sep=0.75pt]    {$O$};
                    		\\draw (578.7,111) node [anchor=north west][inner sep=0.75pt]    {$x$};
                    		\\draw (296,28) node [anchor=north west][inner sep=0.75pt]    {$y$};
                    		\\draw (66.67,129) node [anchor=north west][inner sep=0.75pt]    {$A$};
                    		\\draw (552.15,129) node [anchor=north west][inner sep=0.75pt]    {$B$};
                    	\\end{tikzpicture}
                    \\end{center}
                           Khi đó, parabol đi qua hai điểm $A\\left(-%s; 0\\right)$ và $B\\left(%s; 0\\right)$ nên có phương trình dạng $y = a x^2 + h$ (với $h > 0$ là chiều cao từ đỉnh cầu đến mặt đường, đỉnh parabol là $I(0; h)$). \\\\
                    Ta có parabol đi qua $B\\left(%s; 0\\right) \\Rightarrow a \\cdot %s^2 + h = 0 \\Rightarrow a = -\\frac{h}{%s^2}$. \\\\
                    Phương trình parabol: $y = -\\frac{h}{%s^2}x^2 + h$. \\\\
                    Đạo hàm: $y' = -\\frac{2h}{%s^2}x$. \\\\
                    Độ dốc của mặt cầu đạt giá trị lớn nhất tại hai đầu cầu (tại $x = \\pm %s$). \\\\
                    Độ dốc lớn nhất là $|y'(%s)| = \\left|-\\frac{2h}{%s^2} \\cdot %s\\right| = \\frac{2h}{%s} = \\frac{4h}{%s}$. \\\\
                    Theo giả thiết, độ dốc không vượt quá $%s^\\circ$, nên: \\\\
                    $\\frac{4h}{%s} \\le \\tan %s^\\circ \\Rightarrow h \\le \\frac{%s \\cdot \\tan %s^\\circ}{4} \\approx %s$ (m). \\\\
                    Vậy chiều cao giới hạn từ đỉnh cầu đến mặt đường là khoảng $%s$ m.'''
                         %(latex(L2), latex(L2),
                           latex(L2), latex(L2), latex(L2),
                           latex(L2),
                           latex(L2),
                           latex(L2),
                           latex(L2), latex(L2), latex(L2), latex(L2), latex(L),
                           latex(alpha),
                           latex(L), latex(alpha), latex(L), latex(alpha), kq,
                           kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

