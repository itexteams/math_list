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


def bt_dang20_p1_b3_c2_hh11(self):
            # Khai báo biến
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            # Biến số a ngẫu nhiên (thường dùng trong đề thi)
            val_a = random.randint(1, 5)
            str_a = 'a' if val_a == 1 else str(val_a) + 'a'

            if dang == '1':
                # Góc 45 độ
                sa_latex = str_a + '\\sqrt{2}'
                kq_value = '45^\\circ'
                cac_da_sai = ['60^\\circ', '30^\\circ', '90^\\circ']
                hd_sa = sa_latex
                tan_phi = '1'

            elif dang == '2':
                # Góc 60 độ
                sa_latex = str_a + '\\sqrt{6}'
                kq_value = '60^\\circ'
                cac_da_sai = ['45^\\circ', '30^\\circ', '90^\\circ']
                hd_sa = sa_latex
                tan_phi = '\\sqrt{3}'

            else:
                # Góc 30 độ
                if val_a % 3 == 0:
                    sa_latex = str(val_a // 3) + 'a\\sqrt{6}'
                else:
                    sa_latex = '\\frac{' + str_a + '\\sqrt{6}}{3}'
                kq_value = '30^\\circ'
                cac_da_sai = ['45^\\circ', '60^\\circ', '90^\\circ']
                hd_sa = sa_latex
                tan_phi = '\\frac{\\sqrt{3}}{3}'

            # Thiết lập đáp án
            da_dung = '\\True $' + kq_value + '$'
            list_da = [da_dung]
            for s in cac_da_sai:
                list_da.append('$' + s + '$')
            random.shuffle(list_da)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA$ vuông góc với mặt phẳng $\\left( ABC \\right)$. Biết $SA = %s$. Tam giác $ABC$ vuông cân tại $B$ và $AB = %s$. Góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$ bằng'''
                            %(sa_latex, str_a))

            # Nội dung lời giải
            loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.5,-1.2);
                \\coordinate (C) at (4,0);
                \\coordinate (S) at (0,3);
                \\draw[line width=1pt, dashed] (A)--(C);
                \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B);
                \\filldraw (S)  node[above] {$S$};
                \\filldraw (A)  node[left] {$A$};
                \\filldraw (B)  node[below] {$B$};
                \\filldraw (C)  node[right] {$C$};
                \\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
                \\draw[line width=1pt] (1.35,-0.95)--(1.15,-0.8)--(1.3,-0.65);
            \\end{tikzpicture}
            \\end{center}
            Vì $SA \\perp \\left( ABC \\right)$ nên $AC$ là hình chiếu vuông góc của $SC$ trên mặt phẳng $\\left( ABC \\right)$. \\\\
            Suy ra góc giữa đường thẳng $SC$ và mặt phẳng $\\left( ABC \\right)$ bằng góc giữa $SC$ và $AC$, hay $\\widehat{SCA} = \\varphi$. \\\\
            Xét tam giác $ABC$ vuông cân tại $B$ với $AB = BC = %s$, ta có: \\\\
            $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s\\sqrt{2}$. \\\\
            Xét tam giác $SAC$ vuông tại $A$, ta có: \\\\
            $\\tan \\varphi = \\frac{SA}{AC} = \\frac{%s}{%s\\sqrt{2}} = %s$. \\\\
            Vậy $\\varphi = %s$.'''
                      %(str_a, str_a, str_a, str_a, hd_sa, str_a, tan_phi, kq_value))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_da[0]) + '}\n'
                '{' + str(list_da[1]) + '}\n'
                '{' + str(list_da[2]) + '}\n'
                '{' + str(list_da[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

