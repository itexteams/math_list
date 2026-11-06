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


def bt_dang38_p2_b1_c3_ds12(self):
            # Khai báo biến ký hiệu
            # Khai báo biến
            t = symbols('t')
            v0 = random.choice([30000, 40000, 50000, 60000])
            a = random.choice([500, 1000, 1500, 2000, 2500])
            k = int(a * 3 / 2)
            v1 = 8 * a + v0
            v_c_true = 64 * a + v0
            v_c_false = v_c_true + random.choice([10000, 20000, 34000])
            L = random.choice([300, 400, 500, 600])
            v_d_true = 27 * a - 9 * L + v0
            v_d_false = v_d_true + random.choice([-500, 500, -1000, 1000])
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_bir2oz0cb/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_70yu8pn9w}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            		rgb(37.5bp)=(0.61,0.61,0.61);
            		rgb(50bp)=(0.29,0.29,0.29);
            		rgb(54.15960039411272bp)=(0.61,0.61,0.61);
            		rgb(100bp)=(0.61,0.61,0.61)}
            	\tikzset {_9yrupg0qc/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_3e6aomc4g}{150bp}{rgb(0bp)=(0.29,0.29,0.29);
            		rgb(37.5bp)=(0.29,0.29,0.29);
            		rgb(46.14285605294364bp)=(1,1,1);
            		rgb(53.3749989100865bp)=(0.5,0.5,0.5);
            		rgb(62.03571319580078bp)=(0.29,0.29,0.29);
            		rgb(100bp)=(0.29,0.29,0.29)}
            	\tikzset {_esdd7chw7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_1epzweb9s}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            		rgb(37.5bp)=(0.5,0.5,0.5);
            		rgb(45.8749989100865bp)=(1,1,1);
            		rgb(52.82030923025949bp)=(0.5,0.5,0.5);
            		rgb(61.74999782017299bp)=(0.29,0.29,0.29);
            		rgb(100bp)=(0.29,0.29,0.29)}
            	\tikzset {_dlh8y0v1e/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-89 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_5tpbbz8qb}{150bp}{rgb(0bp)=(0.5,0.5,0.5);
            		rgb(37.5bp)=(0.5,0.5,0.5);
            		rgb(45.8749989100865bp)=(1,1,1);
            		rgb(52.82030923025949bp)=(0.5,0.5,0.5);
            		rgb(61.74999782017299bp)=(0.29,0.29,0.29);
            		rgb(100bp)=(0.29,0.29,0.29)}
            	\tikzset {_1zvpz39hw/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_d2rxvswyh}{150bp}{rgb(0bp)=(0.29,0.29,0.29);
            		rgb(37.5bp)=(0.29,0.29,0.29);
            		rgb(46.14285605294364bp)=(1,1,1);
            		rgb(53.3749989100865bp)=(0.5,0.5,0.5);
            		rgb(62.03571319580078bp)=(0.29,0.29,0.29);
            		rgb(100bp)=(0.29,0.29,0.29)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.56 ] (84.1,232.4) -- (291.6,222.4) -- (260.6,209.9) -- (120.1,202.9) -- (52.6,203.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (282.72,209.6) -- (282.72,218) -- (145.52,225.6) -- (145.52,217.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (145.52,217.2) -- (145.52,225.6) -- (91.92,210.8) -- (92.32,203.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (276.72,208) -- (282.72,209.6) -- (145.52,217.2) -- (147.52,214) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (147.52,214) -- (145.52,217.2) -- (92.32,203.6) -- (97.12,202.8) -- cycle ;
            	\path  [shading=_70yu8pn9w,_bir2oz0cb] (148.32,78.4) -- (147.52,214) -- (97.12,202.8) -- (97.92,92) -- cycle ; 
            	\draw   (148.32,78.4) -- (147.52,214) -- (97.12,202.8) -- (97.92,92) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 65; green, 51; blue, 24 }  ,fill opacity=1 ] (271.92,183.6) -- (274.2,207.33) -- (152.32,213.6) -- (150.2,186.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 65; green, 51; blue, 24 }  ,fill opacity=1 ] (271.52,159.6) -- (271.92,183.6) -- (150.2,186.67) -- (152.2,160.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 99; green, 79; blue, 39 }  ,fill opacity=1 ] (270.72,136) -- (271.52,159.6) -- (152.2,160.67) -- (149.53,135.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 65; green, 51; blue, 24 }  ,fill opacity=1 ] (165.99,37.12) .. controls (186.24,37.12) and (185,53.65) .. (186.25,59.9) .. controls (185.05,65.1) and (180.16,58.48) .. (178.88,62.4) .. controls (176.08,62.8) and (176.85,64.88) .. (169.75,61.4) .. controls (168.78,58.92) and (171,51.9) .. (161.5,52.4) .. controls (156.5,51.9) and (140.37,52.33) .. (131.87,52.33) .. controls (121.53,53.33) and (122.2,60) .. (121.87,71.33) .. controls (121.47,125.33) and (122.56,191) .. (121.68,220) .. controls (118,224.67) and (110,224) .. (106.48,220.8) .. controls (106.48,188.4) and (107.1,84.9) .. (106.53,58.67) .. controls (106.75,48.52) and (118.05,38.37) .. (127.48,37.67) .. controls (154.28,36.87) and (155.49,35.87) .. (165.99,37.12) -- cycle ;
            	\path  [shading=_3e6aomc4g,_9yrupg0qc] (166.6,69.68) -- (166.57,61.46) .. controls (166.57,60.49) and (171.71,59.69) .. (178.04,59.67) .. controls (184.38,59.65) and (189.52,60.42) .. (189.52,61.39) -- (189.55,69.6) .. controls (189.56,70.57) and (184.42,71.38) .. (178.08,71.4) .. controls (171.74,71.42) and (166.6,70.65) .. (166.6,69.68) .. controls (166.6,68.7) and (171.73,67.9) .. (178.07,67.88) .. controls (184.41,67.86) and (189.55,68.63) .. (189.55,69.6) ; 
            	\draw   (166.6,69.68) -- (166.57,61.46) .. controls (166.57,60.49) and (171.71,59.69) .. (178.04,59.67) .. controls (184.38,59.65) and (189.52,60.42) .. (189.52,61.39) -- (189.55,69.6) .. controls (189.56,70.57) and (184.42,71.38) .. (178.08,71.4) .. controls (171.74,71.42) and (166.6,70.65) .. (166.6,69.68) .. controls (166.6,68.7) and (171.73,67.9) .. (178.07,67.88) .. controls (184.41,67.86) and (189.55,68.63) .. (189.55,69.6) ; 
            	\draw  [fill={rgb, 255:red, 113; green, 89; blue, 42 }  ,fill opacity=1 ] (174,69) .. controls (178.67,67.33) and (178.67,69) .. (182,69) .. controls (185.67,90.67) and (193.67,105.33) .. (190.67,110) .. controls (181,103.67) and (180,112.33) .. (171.67,110.33) .. controls (174.33,101) and (178.53,95.33) .. (174,69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 96; green, 75; blue, 35 }  ,fill opacity=1 ] (151.53,104.47) .. controls (157.57,103.88) and (169.45,105.87) .. (190.25,103.87) .. controls (197.37,104.3) and (204.97,106.79) .. (212.65,107.47) .. controls (221.78,108.27) and (231.84,107.19) .. (240.65,107.47) .. controls (252.15,107.83) and (264.61,109.11) .. (273.2,108.8) .. controls (274,132.8) and (272.25,114.67) .. (271.05,135.47) .. controls (213.2,135.47) and (216.27,136.73) .. (149.87,135.13) .. controls (149.47,106.73) and (150.33,132.07) .. (151.53,104.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (153.12,78.4) -- (152.32,213.6) -- (147.52,214) -- (148.32,78.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 189; green, 147; blue, 61 }  ,fill opacity=1 ] (153.53,105.47) .. controls (157.67,105.33) and (171.45,106.87) .. (192.25,104.87) .. controls (199.37,105.3) and (206.97,107.79) .. (214.65,108.47) .. controls (223.78,109.27) and (233.84,108.19) .. (242.65,108.47) .. controls (254.15,108.83) and (262.74,109.31) .. (271.33,109) .. controls (272.13,133) and (272.87,94.87) .. (271.67,115.67) .. controls (263,114.51) and (254,112.33) .. (243.67,115.33) .. controls (231.67,112) and (219.78,112.52) .. (210.33,114) .. controls (199.33,109.67) and (185.07,110.83) .. (179,112.67) .. controls (168.41,112.99) and (160.62,111.16) .. (159,112.67) .. controls (150.33,105.33) and (152.67,115) .. (153.53,105.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 188; green, 149; blue, 74 }  ,fill opacity=1 ] (178.07,67.88) .. controls (182.74,66.21) and (177,68.67) .. (180.33,68.67) .. controls (184,90.33) and (191.33,104.67) .. (188.33,109.33) .. controls (178.67,103) and (188,110.33) .. (179.67,108.33) .. controls (182.33,99) and (182.6,94.21) .. (178.07,67.88) -- cycle ;
            	\draw    (176.47,69.33) .. controls (178.67,80) and (179,94.33) .. (176,104.67) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (271.05,85.67) -- (271.45,89.27) -- (153.05,83.67) -- (153.05,78.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (276.32,85.2) -- (276.72,208) -- (271.4,208.2) -- (271.12,85.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 154; green, 149; blue, 149 }  ,fill opacity=0.32 ] (153.05,83.67) -- (271.45,89.27) -- (271.4,208.2) -- (151.6,210.9) -- cycle ;
            	\path  [shading=_1epzweb9s,_esdd7chw7] (106.48,65.8) -- (121.48,65.8) -- (121.48,223.4) -- (106.48,223.4) -- cycle ; 
            	\draw   (106.48,65.8) -- (121.48,65.8) -- (121.48,223.4) -- (106.48,223.4) -- cycle ; 
            	\path  [shading=_5tpbbz8qb,_dlh8y0v1e] (165.99,37.12) -- (166.21,53.15) -- (127.71,53.7) -- (127.48,37.67) -- cycle ; 
            	\draw   (165.99,37.12) -- (166.21,53.15) -- (127.71,53.7) -- (127.48,37.67) -- cycle ;  
            	\path  [shading=_d2rxvswyh,_1zvpz39hw] (124.17,220.36) -- (124.09,224.98) .. controls (124.08,225.52) and (119.6,225.89) .. (114.07,225.8) .. controls (108.55,225.71) and (104.08,225.19) .. (104.09,224.65) -- (104.17,220.03) .. controls (104.17,219.49) and (108.66,219.12) .. (114.18,219.21) .. controls (119.71,219.3) and (124.18,219.81) .. (124.17,220.36) .. controls (124.16,220.91) and (119.67,221.28) .. (114.15,221.18) .. controls (108.63,221.09) and (104.16,220.58) .. (104.17,220.03) ; 
            	\draw   (124.17,220.36) -- (124.09,224.98) .. controls (124.08,225.52) and (119.6,225.89) .. (114.07,225.8) .. controls (108.55,225.71) and (104.08,225.19) .. (104.09,224.65) -- (104.17,220.03) .. controls (104.17,219.49) and (108.66,219.12) .. (114.18,219.21) .. controls (119.71,219.3) and (124.18,219.81) .. (124.17,220.36) .. controls (124.16,220.91) and (119.67,221.28) .. (114.15,221.18) .. controls (108.63,221.09) and (104.16,220.58) .. (104.17,220.03) ;  
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Một bể chứa dầu ban đầu có $%s$ lít dầu. Gọi $V(t)$ là thể tích dầu trong bể tại thời điểm $t$, trong đó $t$ tính theo giờ và $0 \le t \le 24$. Trong quá trình bơm dầu vào bể, thể tích dầu tăng theo tốc độ được biểu diễn bởi hàm số $V'(t)=k\sqrt{t}$, với $k$ là hằng số dương. Sau $4$ giờ bơm liên tục, thể tích dầu trong bể đạt $%s$ lít.}{%s}'''                  
                             %(latex(v0), latex(v1), hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $V(t)$ là một nguyên hàm của hàm số $f(t)=k\\sqrt{t}$'
            nb_da_1_s = 'Hàm số $f(t)=k\\sqrt{t}$ là một nguyên hàm của hàm số $V(t)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $V'(t) = k\\sqrt{t} = f(t)$. Do đó hàm số $V(t)$ là một nguyên hàm của hàm số $f(t)=k\\sqrt{t}$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $V(t)=\\frac{2k}{3}t\\sqrt{t}+C$, với $0 \\le t \\le 24$ và $k, C$ là các hằng số' 
            th_da_1_s = '$V(t)=\\frac{3k}{2}t\\sqrt{t}+C$, với $0 \\le t \\le 24$ và $k, C$ là các hằng số' 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $V(t) = \\int V'(t) \\text{d}t = \\int k\\sqrt{t} \\text{d}t = \\int k t^{\\frac{1}{2}} \\text{d}t = k \\cdot \\frac{t^{\\frac{3}{2}}}{\\frac{3}{2}} + C = \\frac{2k}{3}t\\sqrt{t}+C$, với $0 \\le t \\le 24$ và $k, C$ là các hằng số.'''       
                            )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Sau $16$ giờ bơm liên tục, thể tích dầu trong bể đạt được $%s$ lít' %(latex(v_c_true))  
            vd_da_1_s = 'Sau $16$ giờ bơm liên tục, thể tích dầu trong bể đạt được $%s$ lít' %(latex(v_c_false))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tại thời điểm ban đầu $t=0$, $V(0) = %s \\Rightarrow C = %s$. \\\\
                            Tại $t=4$, $V(4) = %s \\Rightarrow \\frac{2k}{3}\\cdot 4\\sqrt{4} + %s = %s \\Rightarrow \\frac{16k}{3} = %s \\Rightarrow k = %s$. \\\\
                            Do đó $V(t) = %s t\\sqrt{t} + %s$. \\\\
                            Sau $16$ giờ, thể tích dầu là $V(16) = %s \\cdot 16\\sqrt{16} + %s = %s \\cdot 64 + %s = %s$ (lít).'''  
                       %(latex(v0), latex(v0), latex(v1), latex(v0), latex(v1), latex(v1 - v0), latex(k), latex(a), latex(v0), latex(a), latex(v0), latex(a), latex(v0), latex(v_c_true)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Trong quá trình bơm dầu, nếu sau mỗi giờ lượng dầu bị rò rỉ đều đặn với tốc độ $%s$ lít/giờ thì tại thời điểm $9$ giờ thể tích dầu trong bể là $%s$ lít' %(latex(L), latex(v_d_true)) 
            vdc_da_1_s = 'Trong quá trình bơm dầu, nếu sau mỗi giờ lượng dầu bị rò rỉ đều đặn với tốc độ $%s$ lít/giờ thì tại thời điểm $9$ giờ thể tích dầu trong bể là $%s$ lít' %(latex(L), latex(v_d_false)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $V_1(t)$ là thể tích dầu trong bể khi có rò rỉ. Tốc độ thay đổi thể tích lúc này là \\\\ $V_1'(t) = V'(t) - %s = %s\\sqrt{t} - %s$. \\\\
                            Suy ra $V_1(t) = \\int \\left( %s\\sqrt{t} - %s \\right) \\text{d}t = %s t\\sqrt{t} - %s t + C_1$. \\\\
                            Ban đầu có $%s$ lít dầu nên $C_1 = %s$. Do đó $V_1(t) = %s t\\sqrt{t} - %s t + %s$. \\\\
                            Tại thời điểm $t=9$ giờ, thể tích dầu là \\\\ $V_1(9) = %s \\cdot 9\\sqrt{9} - %s \\cdot 9 + %s = %s \\cdot 27 - %s + %s = %s$ (lít).'''
                       %(latex(L), latex(k), latex(L), latex(k), latex(L), latex(a), latex(L), latex(v0), latex(v0), latex(a), latex(L), latex(v0), latex(a), latex(L), latex(v0), latex(a), latex(L * 9), latex(v0), latex(v_d_true)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                str(noidungcauhoi)+ '\n'+
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

