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


def bt_dang34_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Cấu trúc: (Đường 1, Đường 2, Đường song song với Đường 2, Đỉnh chung tạo tam giác, Tam giác đều)
            bien_the = [
                {
                    'l1': 'AC', 'l2': "A'B", 
                    'l2_parallel': "D'C", 
                    'dinh_chung': 'C', 
                    'tam_giac': "ACD'", 
                    'goc': "ACD'"
                },
                {
                    'l1': 'BD', 'l2': "B'C", 
                    'l2_parallel': "A'D", 
                    'dinh_chung': 'D', 
                    'tam_giac': "BDA'", 
                    'goc': "BDA'"
                },
                {
                    'l1': "A'C'", 'l2': 'CB', 
                    'l2_parallel': "A'B'", 
                    'dinh_chung': "B'", 
                    'tam_giac': "A'B'C'", 
                    'goc': "A'B'C'"
                }
            ]

            # B1-B3: Chọn ngẫu nhiên một bộ dữ liệu
            data = random.choice(bien_the)
            l1 = data['l1']
            l2 = data['l2']
            l2_p = data['l2_parallel']
            tri = data['tam_giac']
            goc_dinh = data['goc']

            # B4: Thiết lập đáp án đúng và các phương án sai (không trùng lặp)
            kq_dung = '$60^\\circ$'
            cac_phuong_an_sai = ['$45^\\circ$', '$90^\\circ$', '$30^\\circ$', '$75^\\circ$', '$120^\\circ$']
            random.shuffle(cac_phuong_an_sai)
            ds_sai = cac_phuong_an_sai[:3]

            # Đưa các đáp án vào danh sách
            da_d = '\\True ' + kq_dung
            list_1 = [da_d] + ds_sai
            random.shuffle(list_1)

            # Phần TikZ để vẽ hình lập phương
            tikz_code = r'''\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, >=stealth]
                \coordinate (A) at (0,0);
                \coordinate (B) at (4,0);
                \coordinate (D) at (1.2,1.2);
                \coordinate (C) at (5.2,1.2);
                \coordinate (A1) at (0,4);
                \coordinate (B1) at (4,4);
                \coordinate (D1) at (1.2,5.2);
                \coordinate (C1) at (5.2,5.2);
                \draw [dashed] (A)--(D)--(C) (D)--(D1);
                \draw (A)--(B)--(C)--(C1)--(D1)--(A1)--cycle;
                \draw (A1)--(B1)--(C1) (B1)--(B);
                \draw [blue, thick] ''' + (r'(A)--(C)' if l1 == 'AC' else r'(B)--(D)' if l1 == 'BD' else r'(A1)--(C1)') + r''';
                \draw [red, thick] ''' + (r"(A1)--(B)" if l2 == "A'B" else r"(B1)--(C)" if l2 == "B'C" else r"(C)--(B)") + r''';
                \draw [green!60!black, dashed, thick] ''' + (r"(D1)--(C)" if l2_p == "D'C" else r"(A1)--(D)" if l2_p == "A'D" else r"(A1)--(B1)") + r''';
                \draw [gray, dashed] ''' + (r"(A)--(D1)" if tri == "ACD'" else r"(B)--(A1)" if tri == "BDA'" else r"(A1)--(C1)") + r''';
                \node [below left] at (A) {$A$};
                \node [below right] at (B) {$B$};
                \node [right] at (C) {$C$};
                \node [above left] at (D) {$D$};
                \node [left] at (A1) {$A'$};
                \node [right] at (B1) {$B'$};
                \node [above right] at (C1) {$C'$};
                \node [above] at (D1) {$D'$};
            \end{tikzpicture}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $%s$ và $%s$ là
            \\begin{center}
            %s
            \\end{center}''' % (l1, l2, tikz_code))

            # Nội dung lời giải chi tiết
            loigiai = ('''Xét hình lập phương $ABCD.A'B'C'D'$. \\\\
            Ta có đường thẳng $%s$ song song với đường thẳng $%s$ (do tứ giác tương ứng là hình bình hành hoặc các cạnh đối diện).\\\\
            Khi đó, góc giữa hai đường thẳng $%s$ và $%s$ chính bằng góc giữa hai đường thẳng $%s$ và $%s$.\\\\
            Xét tam giác $%s$, ta thấy các cạnh của tam giác này đều là các đường chéo của các mặt hình vuông của hình lập phương.\\\\
            Do đó, tam giác $%s$ là tam giác đều, suy ra các góc trong tam giác bằng $60^\\circ$.\\\\
            Vậy góc giữa hai đường thẳng $%s$ và $%s$ bằng góc $\\widehat{%s} = 60^\\circ$.''' 
            % (l2, l2_p, l1, l2, l1, l2_p, tri, tri, l1, l2, goc_dinh))

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

