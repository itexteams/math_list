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


def bt_dang25_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # r là bán kính đường tròn. Trong đề gốc r=4 (AB=8, AD=16)
                # Ta chọn r ngẫu nhiên từ 3 đến 6 để đảm bảo số liệu đẹp
                r = random.randint(3, 6)
                ab = 2 * r
                ad = 4 * r

                # Thiết lập các biểu thức toán học
                # Chọn hệ trục O(0,0) là tâm đường tròn như lời giải mẫu
                # C(r, 0), D(r, ab), A(-3r, ab), B(-3r, 0)
                # Đường tròn: x^2 + (y-r)^2 = r^2
                f_tren = sqrt(r**2 - x**2) + r
                f_duoi = -sqrt(r**2 - x**2) + r
                # Đường thẳng d: y = 2x + 3r
                duong_d = 2*x + 3*r
                # Hoành độ giao điểm: x = -r và x = -3r/5
                x_gd = Rational(-3*r, 5)

                # Tính toán thể tích V1 (Khối tròn xoay tạo bởi cả hình tròn)
                v1_val = pi * integrate(f_tren**2 - f_duoi**2, (x, -r, r))
                v1_num = float(v1_val.evalf())

                # Tính toán thể tích V2 (Phần khối tròn xoay của chỏm bị cắt)
                v2_val = pi * integrate(f_tren**2 - duong_d**2, (x, -r, x_gd))
                v2_num = float(v2_val.evalf())

                # Thể tích cuối cùng
                v_tong = v1_num - v2_num

                # Làm tròn đến hàng đơn vị theo yêu cầu đề bài
                kq_final = int(Decimal(v_tong).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % (kq_final)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = [
                    '$%s$' % (kq_final + random.randint(10, 30)),
                    '$%s$' % (kq_final - random.randint(10, 30)),
                    '$%s$' % (kq_final + random.randint(40, 60)),
                    '$%s$' % (kq_final - random.randint(40, 60)),
                    '$%s$' % (kq_final + 5),
                    '$%s$' % (kq_final - 5)
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại bài toán (Câu hỏi)
                noidungcauhoi = (r'''Từ một tấm bìa giấy hình chữ nhật $ABCD$ có kích thước $AB = %scm, AD = %scm$, người ta vẽ một đường tròn tiếp xúc với ba cạnh $AD, BC, CD$ và kẻ một đường thẳng $d$ cắt đường tròn theo dây $MN$. Biết $d$ cắt cạnh $AD$ tại $P$ sao cho $AP = PC$ và $d$ chia tấm bìa thành hai miền có diện tích bằng nhau.
                                 \begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            \draw (72.67,48.67) -- (274.27,48.67) -- (274.27,148.67) -- (72.67,148.67) -- cycle ;
            \draw [fill={rgb, 255:red, 184; green, 233; blue, 134 } ,fill opacity=1 ] (174.27,98.43) .. controls (174.27,70.98) and (196.52,48.73) .. (223.97,48.73) .. controls (251.42,48.73) and (273.67,70.98) .. (273.67,98.43) .. controls (273.67,125.88) and (251.42,148.13) .. (223.97,148.13) .. controls (196.52,148.13) and (174.27,125.88) .. (174.27,98.43) -- cycle ;
            \draw [fill={rgb, 255:red, 255; green, 255; blue, 255 } ,fill opacity=1 ] (174.47,102.95) .. controls (174.34,101.44) and (174.27,99.91) .. (174.27,98.37) .. controls (174.27,81.32) and (182.82,66.28) .. (195.87,57.31) -- cycle ;
            \draw (213.92,18.96) -- (152.67,148.67) ;
            \draw (55.6,28.8) node [anchor=north west][inner sep=0.75pt] {$A$};
            \draw (56.4,141.4) node [anchor=north west][inner sep=0.75pt] {$B$};
            \draw (274.8,140.2) node [anchor=north west][inner sep=0.75pt] {$C$};
            \draw (273.2,28.4) node [anchor=north west][inner sep=0.75pt] {$D$};
            \draw (151.6,86.8) node [anchor=north west][inner sep=0.75pt] {$M$};
            \draw (170,46.6) node [anchor=north west][inner sep=0.75pt] {$N$};
            \draw (206.8,27.2) node [anchor=north west][inner sep=0.75pt] {$P$};
            \draw (191.6,11.2) node [anchor=north west][inner sep=0.75pt] {$d$};
            \end{tikzpicture}
            \end{center} Quay tấm bìa quanh cạnh $BC$ thì miền phẳng được tô đậm (phần hình tròn nằm phía dưới đường thẳng $d$) tạo thành một vật thể tròn xoay có thể tích (làm tròn đến hàng đơn vị) bằng bao nhiêu?'''
                                 %(latex(ab), latex(ad)))

                # Nội dung lời giải (Sử dụng \text{d}x)
                loigiai = (r"""\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw   (72.67,48.67) -- (274.27,48.67) -- (274.27,148.67) -- (72.67,148.67) -- cycle ;
            					\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (174.27,98.43) .. controls (174.27,70.98) and (196.52,48.73) .. (223.97,48.73) .. controls (251.42,48.73) and (273.67,70.98) .. (273.67,98.43) .. controls (273.67,125.88) and (251.42,148.13) .. (223.97,148.13) .. controls (196.52,148.13) and (174.27,125.88) .. (174.27,98.43) -- cycle ;
            					\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (174.47,102.95) .. controls (174.34,101.44) and (174.27,99.91) .. (174.27,98.37) .. controls (174.27,81.32) and (182.82,66.28) .. (195.87,57.31) -- cycle ;
            					\draw    (213.92,18.96) -- (152.67,148.67) ;
            					\draw    (274.27,148.67) -- (301.52,149.16) ;
            					\draw [shift={(303.52,149.2)}, rotate = 181.04] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (221.52,161.6) -- (221.13,19.2) ;
            					\draw [shift={(221.12,17.2)}, rotate = 89.84] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ; 
            					\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (220.25,98.43) .. controls (220.25,97.68) and (220.86,97.07) .. (221.61,97.07) .. controls (222.36,97.07) and (222.97,97.68) .. (222.97,98.43) .. controls (222.97,99.18) and (222.36,99.79) .. (221.61,99.79) .. controls (220.86,99.79) and (220.25,99.18) .. (220.25,98.43) -- cycle ;
            					\draw (55.6,28.8) node [anchor=north west][inner sep=0.75pt]    {$A$};
            					\draw (56.4,141.4) node [anchor=north west][inner sep=0.75pt]    {$B$};
            					\draw (274.27,148.67) node [anchor=north west][inner sep=0.75pt]    {$C$};
            					\draw (273.2,28.4) node [anchor=north west][inner sep=0.75pt]    {$D$};
            					\draw (151.6,86.8) node [anchor=north west][inner sep=0.75pt]    {$M$};
            					\draw (170,46.6) node [anchor=north west][inner sep=0.75pt]    {$N$};
            					\draw (206.8,27.2) node [anchor=north west][inner sep=0.75pt]    {$P$};
            					\draw (191.6,11.2) node [anchor=north west][inner sep=0.75pt]    {$d$};
            					\draw (202.4,147.2) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (288,133) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (225.6,11.6) node [anchor=north west][inner sep=0.75pt]    {$y$};
            					\draw (223.2,87.2) node [anchor=north west][inner sep=0.75pt]    {$I$};
            				\end{tikzpicture}
            			\end{center}"""
                    '''Chọn $O(0;0)$ là tâm đường tròn, khi đó tọa độ các đỉnh là $A(-%s; %s), B(-%s; 0), C(%s; 0), D(%s; %s)$. \\\\
                             Đường tròn có phương trình $(C): x^2 + (y - %s)^2 = %s$. \\\\
                             Cung trên và dưới của đường tròn có phương trình:
                             $\\begin{cases} (C_1): y = \\sqrt{%s - x^2} + %s \\\\ (C_2): y = -\\sqrt{%s - x^2} + %s \\end{cases}$. \\\\
                             Để $d$ chia tấm bìa thành 2 phần diện tích bằng nhau thì $d$ đi qua tâm hình chữ nhật $M(-%s; %s)$. \\\\
                             Mặt khác $AP = PC$ nên $d$ là đường trung trực của $AC$, phương trình $d: y = 2x + %s$. \\\\
                             Giao điểm của $d$ và cung trên là $x = -%s$ và $x = %s$. \\\\
                             Thể tích khối tròn xoay khi quay hình tròn quanh $BC$: \\\\
                             $V_1 = \\pi \\int_{-%s}^{%s} [(\\sqrt{%s - x^2} + %s)^2 - (-\\sqrt{%s - x^2} + %s)^2] \\text{d}x \\approx %s$. \\\\
                             Thể tích phần chỏm cầu cắt bởi $d$ khi quay quanh $BC$: \\\\
                             $V_2 = \\pi \\int_{-%s}^{%s} [(\\sqrt{%s - x^2} + %s)^2 - (2x + %s)^2] \\text{d}x \\approx %s$. \\\\
                             Thể tích cần tìm là $V = V_1 - V_2 \\approx %s$.'''
                             %(latex(3*r), latex(ab), latex(3*r), latex(r), latex(r), latex(ab),
                               latex(r), latex(r**2),
                               latex(r**2), latex(r), latex(r**2), latex(r),
                               latex(r), latex(r), latex(3*r),
                               latex(r), latex(x_gd),
                               latex(r), latex(r), latex(r**2), latex(r), latex(r**2), latex(r), round(v1_num, 2),
                               latex(r), latex(x_gd), latex(r**2), latex(r), latex(3*r), round(v2_num, 2),
                               kq_final))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_final))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


