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


def bt_dang49_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh a và góc alpha
                a_val = random.choice([2, 4, 5,6, 7, 8])
                alpha_val = random.choice([30, 45, 60])

                a = sp.Integer(a_val)
                alpha = sp.Integer(alpha_val)

                # Tính toán các giá trị bằng SymPy
                # SA = a * cos(alpha)
                SA_val = sp.simplify(a * sp.cos(alpha * sp.pi / 180))
                # SH = SA * sin(alpha)
                SH_val = sp.simplify(SA_val * sp.sin(alpha * sp.pi / 180))

                # Thể tích = 2 * (1/3) * SH_val * S_ADB_val
                # S_ADB = a^2 * sqrt(3) / 4
                S_ADB_val = sp.simplify((a**2) * sp.sqrt(3) / 4)
                V_val = sp.simplify(2 * sp.Rational(1, 3) * SH_val * S_ADB_val)

                # Các đáp án trắc nghiệm gây nhiễu
                s1 = sp.simplify(V_val * 2)
                s2 = sp.simplify(V_val / 2)
                s3 = sp.simplify(V_val * 3)
                s4 = sp.simplify(V_val / 3)
                s5 = sp.simplify(V_val * sp.sqrt(2))
                s6 = sp.simplify(V_val * sp.sqrt(3))

                # Loại bỏ các đáp án trùng với đáp án đúng
                choices_set = {s1, s2, s3, s4, s5, s6}
                choices_set.discard(V_val)
                wrong_choices = random.sample(list(choices_set), 3)

                h1=V_val 
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq).replace('.', ',')

                da = '$%s$' % latex(V_val).replace('.', ',')
                das1 = '$%s$' % latex(wrong_choices[0]).replace('.', ',')
                das2 = '$%s$' % latex(wrong_choices[1]).replace('.', ',')
                das3 = '$%s$' % latex(wrong_choices[2]).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Cho khối chóp $S.ABCD$ có đáy $ABCD$ là hình thoi cạnh $%s$, $\\widehat{ABC}=120^\\circ$, $SB=%s$. Mặt phẳng $(SAD)$ vuông góc với đáy và cạnh bên $SA$ tạo với mặt phẳng đáy một góc $%s^\\circ$. Thể tích khối chóp $S.ABCD$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                                 % (latex(a), latex(a), latex(alpha)))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ (Độ dày nét 1pt, giữ đúng hình dạng)
                tikz_img = '''\\begin{center}
            \\begin{tikzpicture}[line cap=round, line join=round, font=\\footnotesize, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (4,0);
            \\coordinate (D) at (1.5,2);
            \\coordinate (C) at ($(B)+(D)-(A)$);
            \\coordinate (H) at ($(A)!0.3!(D)$);
            \\coordinate (K) at ($(A)!0.5!(D)$);
            \\coordinate (S) at ($(H)+(0,3.5)$);
            \\draw (A) node[left] {$A$} -- (B) node[right] {$B$} -- (C) node[right] {$C$} -- (S) node[above] {$S$} -- cycle;
            \\draw (S) -- (B);
            \\draw[dashed] (A) -- (D) node[above right] {$D$} -- (C);
            \\draw[dashed] (S) -- (D);
            \\draw[dashed] (S) -- (H) node[left] {$H$};
            \\draw[dashed] (B) -- (K) node[left] {$K$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\fill (D) circle (1.5pt);
            \\fill (S) circle (1.5pt);
            \\fill (H) circle (1.5pt);
            \\fill (K) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}'''

                # Nội dung lời giải
                loigiai = ('''%s
            Ta có: $V_{S.ABCD} = 2 \\cdot V_{S.ADB} = 2 \\cdot \\frac{1}{3} \\cdot SH \\cdot S_{ADB}$\\\\
            Tứ giác $ABCD$ có đáy là hình thoi cạnh bằng $%s$ và góc $\\widehat{ABC}=120^\\circ$ nên tam giác $ADB$ là tam giác đều cạnh bằng $%s$\\\\
            Xét khối chóp $B.DSA$ có $BA = BS = BD = %s$ suy ra khối chóp $B.DSA$ là khối chóp có các cạnh bên bằng nhau nên chân đường cao kẻ từ $B$ là điểm $K$ trùng với tâm đường tròn ngoại tiếp $\\Delta DSA$.\\\\
            Mà $(BAD) \\perp (DSA)$ và $\\Delta BDA$ đều nên $BK \\perp AD$ tại điểm $K$ là trung điểm của $AD$.\\\\
            Từ đó ta thấy rằng $K$ là tâm đường tròn ngoại tiếp tam giác $\\Delta DSA$ và là trung điểm của $AD$ nên tam giác $\\Delta DSA$ vuông tại $S$.\\\\
            Suy ra $SA = \\cos \\widehat{SAD} \\cdot AD = \\cos %s^\\circ \\cdot %s = %s$ và $SH = \\sin \\widehat{SAH} \\cdot SA = \\sin %s^\\circ \\cdot %s = %s$\\\\
            Vậy $V_{S.ABCD} = 2 \\cdot V_{S.ADB} = 2 \\cdot \\frac{1}{3} \\cdot SH \\cdot S_{ADB} = 2 \\cdot \\frac{1}{3} \\cdot %s \\cdot (%s)^2 \\cdot \\frac{\\sqrt{3}}{4} = %s \\approx %s.$'''
                           % (tikz_img, latex(a), latex(a), latex(a), latex(alpha), latex(a), latex(SA_val), latex(alpha), latex(SA_val), latex(SH_val), latex(SH_val), latex(a), latex(V_val),kqz))
                dapan='\\shortans[0]{$%s$}\n'%(kqz)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

