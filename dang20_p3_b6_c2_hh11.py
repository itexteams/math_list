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


def bt_dang20_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Random độ dài cạnh đáy (số nguyên)
            lis_k = [3, 4, 5, 6, 7, 8, 9]
            canh_day = random.choice(lis_k)

            # Tính toán các thành phần của bài toán
            # Diện tích đáy S = (canh^2 * sqrt(3)) / 4
            s_day = (canh_day**2 * sp.sqrt(3)) / 4

            # Bán kính đường tròn ngoại tiếp đáy AO = (canh * sqrt(3)) / 3
            ao = (canh_day * sp.sqrt(3)) / 3

            # Chiều cao SO = AO * tan(45) = AO
            so = ao

            # Thể tích V = 1/3 * SO * S_day
            v_exact = sp.Rational(1, 3) * so * s_day

            # Chuyển đổi sang số thập phân làm tròn 1 chữ số
            v_decimal = round(float(v_exact.evalf()), 1)

            # Bước 4: Điều chỉnh các phương án sai (cũng làm tròn 1 chữ số)
            da_dung = f"{v_decimal}"

            # Tạo các phương án nhiễu
            sai1_val = round(float((so * s_day).evalf()), 1) # Quên 1/3
            sai2_val = round(float((sp.Rational(1, 3) * (canh_day * sp.sqrt(3) / 2) * s_day).evalf()), 1) # Nhầm AO
            sai3_val = round(float((v_exact * 1.5).evalf()), 1) # Sai số ngẫu nhiên

            # Đảm bảo các phương án không trùng nhau
            list_val_sai = list(set([sai1_val, sai2_val, sai3_val]))
            while len(list_val_sai) < 3:
                list_val_sai.append(round(v_decimal + random.uniform(1.0, 5.0), 1))

            sai1 = f"{list_val_sai[0]}"
            sai2 = f"{list_val_sai[1]}"
            sai3 = f"{list_val_sai[2]}"

            list_sai = [sai1, sai2, sai3]
            random.shuffle(list_sai)

            # Nội dung câu hỏi
            noidungcauhoi = (f'Cho một hình chóp tam giác đều có cạnh đáy bằng ${canh_day}$, '
                             f'góc giữa cạnh bên và mặt phẳng đáy bằng $45^\\circ$. '
                             f'Thể tích khối chóp đó bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).')

            # Hình vẽ TikZ
            ve_hinh = r'''\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1] 
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (93.88,138.89) -- (253.23,138.89) ;
            	\draw [line width=1]    (93.88,138.89) -- (139.41,184.41) ;
            	\draw [line width=1]    (139.41,184.41) -- (253.23,138.89) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (93.88,138.89) -- (196.32,161.65) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (162.17,154.82) -- (162.17,47.83) ; 
            	\draw [line width=1]    (162.17,47.83) -- (93.88,138.89) ;
            	\draw [line width=1]    (162.17,47.83) -- (139.41,184.41) ;
            	\draw [line width=1]    (162.17,47.83) -- (253.23,138.89) ;
            	\draw (155.92,24.92) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\draw (74.11,125.08) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (128.6,187.69) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (258.43,123.95) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (197.77,163.1) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\draw (146.35,151.72) node [anchor=north west][inner sep=0.75pt]    {$O$};
            \end{tikzpicture}
            \end{center}'''

            # Lời giải chi tiết
            loigiai = (ve_hinh + 'Gọi $O$ là tâm của đáy $ABC \\Rightarrow SO \\perp \\left(ABC\\right)$.\\\\ '
                       f'Vì $S.ABC$ là hình chóp tam giác đều nên $ABC$ là tam giác đều cạnh ${canh_day}$.\\\\ '
                       f'Diện tích tam giác đáy là: $S_{{ABC}} = \\frac{{{canh_day}^2\\sqrt{{3}}}}{{4}} = {sp.latex(s_day)}$.\\\\ '
                       f'Bán kính đường tròn ngoại tiếp đáy: $AO = \\frac{{{canh_day}\\sqrt{{3}}}}{{3}} = {sp.latex(ao)}$.\\\\ '
                       'Góc giữa cạnh bên $SA$ và mặt đáy là $\\widehat{SAO} = 45^\\circ$.\\\\ '
                       f'Trong tam giác vuông $SAO$: $SO = AO \\cdot \\tan 45^\\circ = {sp.latex(ao)}$.\\\\ '
                       f'Thể tích khối chóp là: $V = \\frac{{1}}{{3}} \\cdot SO \\cdot S_{{ABC}} = \\frac{{1}}{{3}} \\cdot {sp.latex(ao)} \\cdot {sp.latex(s_day)} = {sp.latex(v_exact)} \\approx {v_decimal}$.')

            # Trộn đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(v_decimal).replace('.', ','))
            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

