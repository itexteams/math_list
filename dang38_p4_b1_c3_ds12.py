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


def bt_dang38_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                # Chọn ngẫu nhiên hệ số a (nên là số chẵn để biểu thức đẹp)
                a = random.choice([2, 4, 6, 8])
                # Chọn hệ số K trong f(pi/4) = (K*sqrt(2))/4
                K = random.randint(3, 15)

                C_val = Rational(K, 2)


                kq_num = a + 4*K
                kq_den = 16
                kq_frac = Rational(kq_num, kq_den)

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Đáp án đúng
                da = '$%s$' % latex(kq_frac)

                # Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_num = kq_num + random.choice([-2, -1, 1, 2, 3])
                    if sai_num > 0:
                        phi_sai = '$%s$' % latex(Rational(sai_num, kq_den))
                        if phi_sai != da:
                            s.add(phi_sai)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- BƯỚC 2: VIẾT LẠI ĐỀ BÀI VÀ LỜI GIẢI ---
                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $\mathbb{R}$, thỏa mãn $f\left( \frac{\pi}{4} \right) = \frac{%s\sqrt{2}}{4}$ và $\cos x \cdot f'(x) + \sin x \cdot f(x) = %s \sin x \cdot \cos^3 x$ với mọi $x \in \left( 0;\frac{\pi}{2} \right)$. Tính $f\left( \frac{\pi}{3} \right)$.'''
                                 % (latex(K), latex(a)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có: $\cos x \cdot f'(x) + \sin x \cdot f(x) = %s \sin x \cdot \cos^3 x$ \\
                             $\Leftrightarrow \frac{\cos x \cdot f'(x) + \sin x \cdot f(x)}{\cos^2 x} = %s \sin x \cdot \cos x = %s \sin 2x$ \\
                             $\Leftrightarrow \left[ \frac{f(x)}{\cos x} \right]' = %s \sin 2x \Rightarrow \frac{f(x)}{\cos x} = -\frac{%s}{2} \cos 2x + C$. \\
                             Thay $x = \frac{\pi}{4}$: $f\left( \frac{\pi}{4} \right) = \cos \frac{\pi}{4} \left( -\frac{%s}{2} \cos \frac{\pi}{2} + C \right) = \frac{\sqrt{2}}{2} C$. \\
                             Theo giả thiết $f\left( \frac{\pi}{4} \right) = \frac{%s\sqrt{2}}{4} \Rightarrow \frac{\sqrt{2}}{2} C = \frac{%s\sqrt{2}}{4} \Rightarrow C = \frac{%s}{2}$. \\
                             Khi đó: $f\left( \frac{\pi}{3} \right) = \cos \frac{\pi}{3} \left( -\frac{%s}{2} \cos \frac{2\pi}{3} + \frac{%s}{2} \right) = \frac{1}{2} \left( \frac{%s}{4} + \frac{%s}{2} \right) = %s$.'''
                           % (latex(a), latex(a), latex(a//2) if a%2==0 else latex(Rational(a,2)), 
                              latex(a//2) if a%2==0 else latex(Rational(a,2)), 
                              latex(a//2) if a%2==0 else latex(Rational(a,2)),
                              latex(a//2) if a%2==0 else latex(Rational(a,2)),
                              latex(K), latex(K), latex(K),
                              latex(a//2) if a%2==0 else latex(Rational(a,2)),
                              latex(K), latex(a//2) if a%2==0 else latex(Rational(a,2)),
                              latex(K), latex(kq_frac)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

