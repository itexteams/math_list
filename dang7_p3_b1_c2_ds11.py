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


def bt_dang7_p3_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá trị M mà tổng u cần vượt qua
                M = random.randint(1500, 3000)

                # Tính toán giá trị ngưỡng 16*M/pi
                val = 16 * M / math.pi

                # Tìm n chẵn nhỏ nhất thỏa mãn n(n+1) > 16M/pi
                n_ans = 2
                while n_ans * (n_ans + 1) <= val:
                    n_ans += 2

                kq = n_ans
                val_round = str(round(val, 2)).replace('.', ',')

                # Các đáp án trắc nghiệm nhiễu
                s = [kq + 2, kq - 2, kq + 4, kq - 4]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trên trục $Ox$ lấy các điểm $A_1, A_2, \\dots, A_n, \\dots$ sao cho $OA_n = n$, với mỗi số nguyên dương $n$. Trong cùng một nửa mặt phẳng có bờ là đường thẳng chứa trục $Ox$, vẽ các nửa đường tròn đường kính $OA_n$ với $n = 1, 2, 3, \\dots$\\\\
            Kí hiệu:
            \\begin{itemize}
                \\item $u_1$ là diện tích của nửa hình tròn đường kính $OA_1$.
                \\item $u_n$ là diện tích của hình giới hạn bởi nửa đường tròn đường kính $OA_{n-1}$, nửa đường tròn đường kính $OA_n$ và tia $Ox$, với mỗi $n = 2, 3, \\dots$ (tham khảo hình vẽ).
            \\end{itemize}
            \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (198.4,42.4) .. controls (287.72,42.4) and (360.13,114.81) .. (360.13,204.13) -- (36.67,204.13) .. controls (36.67,114.81) and (109.08,42.4) .. (198.4,42.4) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (177.73,63.47) .. controls (255.42,63.47) and (318.4,126.45) .. (318.4,204.13) -- (37.07,204.13) .. controls (37.07,126.45) and (100.05,63.47) .. (177.73,63.47) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (158.38,83.47) .. controls (225.03,83.47) and (279.05,137.49) .. (279.05,204.13) -- (37.72,204.13) .. controls (37.72,137.49) and (91.74,83.47) .. (158.38,83.47) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (138.39,103.46) .. controls (193.99,103.46) and (239.07,148.53) .. (239.07,204.13) -- (37.72,204.13) .. controls (37.72,148.53) and (82.79,103.46) .. (138.39,103.46) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (138.4,103.47) .. controls (194,103.47) and (239.07,148.54) .. (239.07,204.13) -- (37.73,204.13) .. controls (37.73,148.54) and (82.8,103.47) .. (138.4,103.47) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (118.38,123.47) .. controls (162.93,123.47) and (199.05,159.58) .. (199.05,204.13) -- (37.72,204.13) .. controls (37.72,159.58) and (73.83,123.47) .. (118.38,123.47) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (97.72,144.13) .. controls (130.85,144.13) and (157.71,170.99) .. (157.71,204.13) -- (37.72,204.13) .. controls (37.72,170.99) and (64.58,144.13) .. (97.72,144.13) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (77.73,164.12) .. controls (99.82,164.12) and (117.73,182.03) .. (117.73,204.13) -- (37.72,204.13) .. controls (37.72,182.03) and (55.64,164.12) .. (77.73,164.12) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (57.4,184.45) .. controls (68.26,184.45) and (77.07,193.26) .. (77.07,204.13) -- (37.72,204.13) .. controls (37.72,193.26) and (46.53,184.45) .. (57.4,184.45) -- cycle ;
            		\\draw [line width=1]    (36.67,204.13) -- (385.07,204.13) ;
            		\\draw [shift={(389.07,204.13)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
            		\\draw (15.33,197.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\\draw (378,211) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\\draw (70,209) node [anchor=north west][inner sep=0.75pt]    {$1$};
            		\\draw (108.67,209) node [anchor=north west][inner sep=0.75pt]    {$2$};
            		\\draw (149.33,209) node [anchor=north west][inner sep=0.75pt]    {$3$};
            		\\draw (190.67,209) node [anchor=north west][inner sep=0.75pt]    {$4$};
            		\\draw (232,209) node [anchor=north west][inner sep=0.75pt]    {$5$};
            		\\draw (271.33,209) node [anchor=north west][inner sep=0.75pt]    {$6$};
            		\\draw (310.67,209) node [anchor=north west][inner sep=0.75pt]    {$7$};
            		\\draw (352.67,209) node [anchor=north west][inner sep=0.75pt]    {$8$};
            		\\draw (48,189) node [anchor=north west][inner sep=0.75pt]    {$u_{1}$};
            		\\draw (84.67,189) node [anchor=north west][inner sep=0.75pt]    {$u_{2}$};
            		\\draw (126,189) node [anchor=north west][inner sep=0.75pt]    {$u_{3}$};
            		\\draw (166,189) node [anchor=north west][inner sep=0.75pt]    {$u_{4}$};
            		\\draw (210,189) node [anchor=north west][inner sep=0.75pt]    {$u_{5}$};
            		\\draw (248.67,189) node [anchor=north west][inner sep=0.75pt]    {$u_{6}$};
            		\\draw (286.67,189) node [anchor=north west][inner sep=0.75pt]    {$u_{7}$};
            		\\draw (330,189) node [anchor=north west][inner sep=0.75pt]    {$u_{8}$};
            		\\draw (65.33,225) node [anchor=north west][inner sep=0.75pt]    {$A_{1}$};
            		\\draw (104.67,225) node [anchor=north west][inner sep=0.75pt]    {$A_{2}$};
            		\\draw (146,225) node [anchor=north west][inner sep=0.75pt]    {$A_{3}$};
            		\\draw (188.67,225) node [anchor=north west][inner sep=0.75pt]    {$A_{4}$};
            		\\draw (228.67,225) node [anchor=north west][inner sep=0.75pt]    {$A_{5}$};
            		\\draw (267.33,225) node [anchor=north west][inner sep=0.75pt]    {$A_{6}$};
            		\\draw (308,222.33) node [anchor=north west][inner sep=0.75pt]    {$A_{7}$};
            		\\draw (348.67,225) node [anchor=north west][inner sep=0.75pt]    {$A_{8}$};
            	\\end{tikzpicture}
            \\end{center}
            Hỏi khi $n$ bằng bao nhiêu thì tổng $u_2 + u_4 + \\dots + u_n$ bắt đầu lớn hơn $%s$?'''
                                 % (latex(M)))

                # Các đáp án
                da_d = ('\\True $%s$' % kq)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Bán kính của nửa đường tròn đường kính $OA_n$ là $R_n = \\frac{n}{2}$.\\\\
            Diện tích của nửa đường tròn đường kính $OA_n$ là $S_n = \\frac{1}{2} \\pi R_n^2 = \\frac{\\pi n^2}{8}$.\\\\
            Theo đề bài, diện tích $u_n$ là phần giới hạn giữa nửa đường tròn $OA_n$ và $OA_{n-1}$, do đó: \\\\
            $u_n = S_n - S_{n-1} = \\frac{\\pi n^2}{8} - \\frac{\\pi (n-1)^2}{8} = \\frac{\\pi}{8}(2n - 1)$ với mọi $n \\ge 2$.\\\\
            Tổng các diện tích với chỉ số chẵn từ $2$ đến $n$ (do dãy cộng đến $u_n$ nên $n$ là số chẵn, đặt $n = 2k$, $k \\in \\mathbb{N}^*$) là:\\\\
            $T = u_2 + u_4 + \\dots + u_n = \\sum_{j=1}^{k} u_{2j} = \\sum_{j=1}^{k} \\frac{\\pi}{8} (4j - 1) = \\frac{\\pi}{8} \\left( 4 \\cdot \\frac{k(k+1)}{2} - k \\right) = \\frac{\\pi}{8} (2k^2 + k)$.\\\\
            Thay $k = \\frac{n}{2}$, ta được:\\\\
            $T = \\frac{\\pi}{8} \\left( 2\\left(\\frac{n}{2}\\right)^2 + \\frac{n}{2} \\right) = \\frac{\\pi n(n+1)}{16}$.\\\\
            Để tổng này bắt đầu lớn hơn $%s$, ta cần có: \\\\
            $\\frac{\\pi n(n+1)}{16} > %s \\Leftrightarrow n(n+1) > \\frac{16 \\cdot %s}{\\pi} \\approx %s$.\\\\
            Vì $n$ là số nguyên dương chẵn, giá trị chẵn nhỏ nhất thỏa mãn bất phương trình trên là $n = %s$.'''
                           % (latex(M), latex(M), latex(M), val_round, latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

