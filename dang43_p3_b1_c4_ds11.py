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


def bt_dang43_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random độ dài cạnh OM = ON (L)
                # Chọn L sao cho L^2 chia hết cho 3 hoặc để dạng phân số cho đẹp
                L = random.choice([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

                # Tính toán các thông số
                a1 = Rational(L, 2)
                a2 = Rational(L, 4)
                a3 = Rational(L, 8)

                s1 = a1**2
                s2 = a2**2
                s3 = a3**2

                q = Rational(1, 4)
                tong_s = s1 / (1 - q)

                # Đáp án đúng
                da = '$%s$' % latex(tong_s)

                # Các đáp án nhiễu (distractors)
                s_nhieu = [
                    '$%s$' % latex(s1),                # Chỉ tính hình vuông đầu
                    '$%s$' % latex(Rational(L**2, 2)), # Sai công thức (L^2/2)
                    '$%s$' % latex(Rational(L**2, 4)), # Sai công thức (L^2/4)
                    '$%s$' % latex(Rational(L**2, 6)), # Sai mẫu số
                    '$%s$' % latex(2 * tong_s),         # Gấp đôi kết quả
                    '$%s$' % latex(tong_s + 1)
                ]

                random.shuffle(s_nhieu)
                das1 = s_nhieu[0]
                das2 = s_nhieu[1]
                das3 = s_nhieu[2]

                # ---------------------------------------------------------
                # B2: Viết lại nội dung bài toán theo mẫu code
                # ---------------------------------------------------------

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Cho tam giác $OMN$ vuông cân tại $O$, $OM = ON = %s$. Trong tam giác $OMN$, vẽ hình vuông $OA_1B_1C_1$ sao cho các đỉnh $A_1, B_1, C_1$ lần lượt nằm trên các cạnh $OM, MN, ON$. Trong tam giác $A_1MB_1$, vẽ hình vuông $A_1A_2B_2C_2$ sao cho các đỉnh $A_2, B_2, C_2$ lần lượt nằm trên các cạnh $A_1M, MB_1, A_1B_1$. Tiếp tục quá trình đó mãi mãi, ta được một dãy các hình vuông. Tổng diện tích các hình vuông này bằng bao nhiêu?}
                                 {\begin{tikzpicture}
        	\coordinate (O) at (0,0);
        	\pgfmathsetmacro{\H}{6}
        	\pgfmathsetmacro{\L}{6}
        	\coordinate (N) at (0,\H);
        	\coordinate (M) at (\L,0);
        	\coordinate (A1) at (3,0);
        	\coordinate (C1) at (0,3);
        	\coordinate (B1) at (3,3);
        	\coordinate (A2) at (4.5,0);
        	\coordinate (C2) at (3,1.5);
        	\coordinate (B2) at (4.5,1.5);
        	\coordinate (A3) at (5.25,0);
        	\coordinate (C3) at (4.5,0.75);
        	\coordinate (B3) at (5.25,0.75);
        	\draw[line width=1pt] (N)--(O)--(M)--cycle;
        	\draw[line width=1pt] (C1)--(B1)--(A1);
        	\draw[line width=1pt] (C2)--(B2)--(A2);
        	\draw[line width=1pt] (C3)--(B3)--(A3);
        	\node[below left] at (O) {$O$};
        	\node[above left] at (N) {$N$};
        	\node[below right] at (M) {$M$};
        	\node[below] at (A1) {$A_1$};
        	\node[above right] at (B1) {$B_1$};
        	\node[left] at (C1) {$C_1$};
        	\node[below] at (A2) {$A_2$};
        	\node[above right] at (B2) {$B_2$};
        	\node[left] at (C2) {$C_2$};
        	\node[below] at (A3) {$A_3$};
        	\node[above right] at (B3) {$B_3$};
        	\node[left] at (C3) {$C_3$};
        \end{tikzpicture}}'''
                                  % (latex(L)))

                # Nội dung lời giải
                loigiai = ('''Độ dài cạnh của các hình vuông lần lượt là $a_1 = \\frac{%s}{2}; a_2 = \\frac{%s}{4}; a_3 = \\frac{%s}{8}; \\dots$ \\\\
                             Diện tích của các hình vuông lần lượt là $S_1 = \\left(\\frac{%s}{2}\\right)^2; S_2 = \\left(\\frac{%s}{4}\\right)^2; S_3 = \\left(\\frac{%s}{8}\\right)^2; \\dots$ \\\\
                             Các diện tích $S_1; S_2; S_3; \\dots$ tạo thành cấp số nhân lùi vô hạn với số hạng đầu là $S_1 = %s$ và công bội là $q = \\frac{1}{4}$. \\\\
                             Do đó, tổng diện tích các hình vuông là $S = \\frac{%s}{1 - \\frac{1}{4}} = %s$.'''
                           % (latex(L), latex(L), latex(L), 
                              latex(L), latex(L), latex(L), 
                              latex(s1), latex(s1), latex(tong_s)))

                # Đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(tong_s))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

