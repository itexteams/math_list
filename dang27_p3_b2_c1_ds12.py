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


def bt_dang27_p3_b2_c1_ds12(self):
            # Khai báo biến
            R = symbols('R')
            Chuvi = round(random.uniform(1.4, 3.5), 2) # Chu vi ngẫu nhiên
            C = Chuvi

            #Tên
            ds_ten = [
                "Minh", "Khoa", "Đạt", "Huy", "Long", "Phúc", "Quân", "Nam", "Bảo", "Duy",
                "Lan", "Mai", "Vy", "Ngọc", "Trang", "Linh", "Hương", "Thảo", "Nhi", "An"
            ]
            ten = random.choice(ds_ten)
            # Độ dài cung
            l = C - 2*R

            # Diện tích lát pizza
            dt = (1/2) * R * l
            S = simplify(dt)

            # Đạo hàm 
            dS = diff(S, R)
            Rmin = C / 4

            def tp_vn(value):
                """Chuyển đổi số thành dạng có dấu phẩy và bỏ .0 nếu cần"""
                return str(int(value)) if value == int(value) else str(value).replace('.', ',')

            def round_vn(so):
                so = Decimal(str(so))

                if so == so.to_integral_value():
                    return (str(so.to_integral_value()), 'hàng đơn vị')

                lam_tron_1 = so.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                s1 = str(lam_tron_1).replace('.', ',')
                if len(s1) <= 4:
                    return (s1, 'hàng phần mười')

                lam_tron_2 = so.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                s2 = str(lam_tron_2).replace('.', ',')
                if len(s2) <= 4:
                    return (s2, 'hàng phần trăm')

                return (str(so.to_integral_value()), 'hàng đơn vị')

            R_text, mo_ta = round_vn(2*Rmin)

            # ===== Nội dung câu hỏi =====
            noidungcauhoi = f"""\\immini{{
            Bạn {ten} được tặng một lát Pizza hình quạt có chu vi bằng {tp_vn(C)} dm (hình vẽ minh hoạ). Bánh Pizza có đường kính bao nhiêu dm để bạn {ten} nhận được lát bánh lớn nhất (tức là lát bánh có diện tích lớn nhất)? (Kết quả làm tròn đến {mo_ta}).}}
            {{	\\begin{{tikzpicture}}[scale=0.6]
                    \\draw[thick] (0,0) circle (3cm);
                    \\coordinate (O) at (0,0);
                    \\coordinate (A) at (3,0);
                    \\coordinate (B) at (60:3);
                    \\fill[blue!60] (A) -- (O) -- (B) arc (60:0:3);
                    \\draw[thick] (O) -- (A);
                    \\draw[thick] (O) -- (B);
                    \\node at (3.7,2) {{\\textbf{{Pizza}}}};
                    \\coordinate (R) at ($(O)!0.5!(A)$);
                    \\node[below] at (R) {{$R$}};
                    \\fill (O) circle (2pt);
                    \\node[left] at (O) {{$O$}};
                \\end{{tikzpicture}}
            }}"""
            # ===== Nội dung lời giải chi tiết =====
            loigiai = rf"""Gọi $R$ (dm) là bán kính của bánh Pizza, điều kiện: $R>0$.\\
            Chu vi lát bánh Pizza là $C={tp_vn(C)}=2R+l \Rightarrow l=C-2R$, với $l$ là độ dài cung tròn của bánh.\\
            Diện tích lát pizza: $S(R)=\frac{{1}}{{2}} R l = \frac{{1}}{{2}} R(C-2R)=\frac{{1}}{{2}}RC-R^2$.\\
            Suy ra $S'(R) = \frac{{1}}{{2}}C-2R$.\\
            Phương trình $S'(R)=0$ có nghiệm $R=\dfrac{{C}}{{4}}$.\\
            Vì hàm số $S(R)$ đồng biến trên khoảng $\left(0; \dfrac{{C}}{{4}}\right)$ và nghịch biến trên khoảng $\left(\dfrac{{C}}{{4}};+\infty\right)$ nên $S(R)$ đạt giá trị lớn nhất tại $R=\dfrac{{C}}{{4}}$.\\
            Vậy đường kính bánh Pizza cần có là $2R=\dfrac{{C}}{{2}} \approx {R_text}$ dm."""

            # ===== Đáp án ngắn gọn (LaTeX) =====
            dapan = r'\shortans[0]{$%s$}' % sp.latex(R_text)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

