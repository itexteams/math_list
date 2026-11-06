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


def bt_dang28_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho sympy
            a_sym = symbols('a')

            # Bước 3: Suy nghĩ tìm cách random bài toán
            # Random hệ số k của cạnh đáy (ví dụ: a, 2a, 3a...)
            lis_k = [1, 2, 3, 4]
            k = random.choice(lis_k)
            canh_day = k * a_sym

            # Tính toán các thành phần của bài toán
            # Diện tích đáy S = (canh^2 * sqrt(3)) / 4
            s_day = sp.simplify((canh_day**2 * sqrt(3)) / 4)

            # Bán kính đường tròn ngoại tiếp đáy AO = (canh * sqrt(3)) / 3
            ao = sp.simplify((canh_day * sqrt(3)) / 3)

            # Chiều cao SO = AO * tan(45) = AO
            so = ao

            # Thể tích V = 1/3 * SO * S_day
            v_exact = sp.simplify(Rational(1, 3) * so * s_day)

            # Bước 4: Điều chỉnh các phương án sai
            # Đáp án đúng
            da_dung = '$' + latex(v_exact) + '$'

            # Tạo các phương án nhiễu (sai lầm thường gặp)
            sai1 = '$' + latex(sp.simplify(so * s_day)) + '$' # Quên 1/3
            sai2 = '$' + latex(sp.simplify(Rational(1, 3) * (canh_day * sqrt(3) / 2) * s_day)) + '$' # Nhầm AO với đường cao tam giác đáy
            sai3 = '$' + latex(sp.simplify(v_exact / sqrt(3))) + '$' # Thiếu căn 3

            list_sai = [sai1, sai2, sai3]
            random.shuffle(list_sai)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho một hình chóp tam giác đều có cạnh đáy bằng $%s$, góc giữa cạnh bên và mặt phẳng đáy bằng $45^\\circ$. Thể tích khối chóp đó là'
                             % (latex(canh_day)))

            # Hình vẽ TikZ giống 100% ảnh (độ dày 1pt)
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

            # Lời giải chi tiết theo mẫu
            loigiai = (ve_hinh + 'Gọi $O$ là tâm của đáy $ABC \\Rightarrow SO \\perp \\left(ABC\\right)$.\\\\ '
                       'Vì $S.ABC$ là hình chóp tam giác đều nên $ABC$ là tam giác đều cạnh $%s$.\\\\ '
                       'Diện tích tam giác đáy là: $S_{ABC} = \\frac{\\left(%s\\right)^2\\sqrt{3}}{4} = %s$.\\\\ '
                       'Bán kính đường tròn ngoại tiếp tam giác đáy là: $AO = \\frac{%s \\cdot \\sqrt{3}}{3} = %s$.\\\\ '
                       'Góc giữa cạnh bên $SA$ và mặt đáy là $\\left(SA; \\left(ABC\\right)\\right) = \\widehat{SAO} = 45^\\circ$.\\\\ '
                       'Trong tam giác vuông $SAO$, ta có chiều cao: $SO = AO \\cdot \\tan 45^\\circ = %s \\cdot 1 = %s$.\\\\ '
                       'Thể tích khối chóp là: $V = \\frac{1}{3} \\cdot SO \\cdot S_{ABC} = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'
                       % (latex(canh_day), latex(canh_day), latex(s_day), 
                          latex(canh_day), latex(ao), 
                          latex(ao), latex(so),
                          latex(so), latex(s_day), latex(v_exact)))

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

