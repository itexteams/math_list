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


def bt_dang36_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cạnh đáy a và hệ số k để cạnh bên h = 2*k*a
                # Trong đề bài gốc: a = 1, h = 2 (tương ứng k = 1)
                a = random.randint(1, 3)
                k = random.randint(1, 3)
                h = 2 * k * a

                # Tính toán các cạnh của tam giác ABC1
                # BC1_bp = a^2 + (h/2)^2
                h_half = Rational(h, 2)
                bc1_sq = a**2 + h_half**2
                bc1_val = sqrt(bc1_sq)

                # Tính cosin
                # cos_B = a / (2 * bc1_val)
                cos_val = simplify(Rational(a, 1) / (2 * bc1_val))

                # Đáp án đúng
                kq = '$%s$' % latex(cos_val)

                # Tạo các đáp án nhiễu
                s = []
                # Nhiễu 1: Nghịch đảo hoặc sai hệ số
                s.append('$%s$' % latex(simplify(Rational(a, 1) / bc1_val)))
                # Nhiễu 2: Thay bằng sin (nếu có thể)
                s.append('$%s$' % latex(simplify(h_half / bc1_val)))
                # Nhiễu 3: Một giá trị ngẫu nhiên phổ biến trong hình học
                s.append('$%s$' % latex(simplify(sqrt(3) * cos_val)))
                # Nhiễu 4: Thêm các giá trị khác để đảm bảo đủ 3 đáp án sai
                s.append('$\\frac{\\sqrt{2}}{2}$')
                s.append('$\\frac{\\sqrt{3}}{2}$')
                s.append('$\\frac{1}{2}$')

                # Lọc bỏ đáp án trùng với đáp án đúng
                s = [item for item in s if item != kq]
                # Lấy ngẫu nhiên 3 đáp án sai duy nhất
                wrong_choices = random.sample(list(set(s)), 3)

                das1, das2, das3 = wrong_choices

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lăng trụ đều $ABC.A'B'C'$ có cạnh đáy bằng $%s$, cạnh bên bằng $%s$. Gọi $C_1$ là trung điểm của $CC'$. Côsin của góc giữa hai đường thẳng $BC_1$ và $A'B'$ bằng'''
                                 %(latex(a), latex(h)))

                # Các đáp án
                da_d = ('\\True ' + str(kq))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có $A'B' \\parallel AB$ nên góc giữa hai đường thẳng $BC_1$ và $A'B'$ bằng góc giữa hai đường thẳng $BC_1$ và $AB$.\\\\
                           Xét tam giác $ABC_1$ ta có:\\\\
                           $AB = %s$.\\\\
                           $CC' = %s \\Rightarrow CC_1 = \\frac{1}{2}CC' = %s$.\\\\
                           Trong tam giác vuông $BCC_1$ (vuông tại $C$): $BC_1 = \\sqrt{BC^2 + CC_1^2} = \\sqrt{%s^2 + %s^2} = %s$.\\\\
                           Trong tam giác vuông $ACC_1$ (vuông tại $C$): $AC_1 = \\sqrt{AC^2 + CC_1^2} = \\sqrt{%s^2 + %s^2} = %s$.\\\\
                           Áp dụng hệ quả định lý côsin trong tam giác $ABC_1$:\\\\
                           $\\cos \\widehat{ABC_1} = \\frac{AB^2 + BC_1^2 - AC_1^2}{2 \\cdot AB \\cdot BC_1} = \\frac{%s^2 + (%s)^2 - (%s)^2}{2 \\cdot %s \\cdot %s} = %s$.\\\\
                           Vì $%s > 0$ nên góc $\\widehat{ABC_1}$ là góc nhọn, vậy côsin góc giữa hai đường thẳng là $%s$.'''
                           %(latex(a), latex(h), latex(h_half), 
                             latex(a), latex(h_half), latex(bc1_val),
                             latex(a), latex(h_half), latex(bc1_val),
                             latex(a), latex(bc1_val), latex(bc1_val), latex(a), latex(bc1_val), latex(cos_val),
                             latex(cos_val), latex(cos_val)
                            ))

                # Mã TikZ vẽ hình
                tikz_code = ('''
            \\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round]
                % Định nghĩa tọa độ các đỉnh đáy
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-0.8);
                \\coordinate (C) at (3,0);
                \\def\\h{3.5}
                \\coordinate (A1) at (0,\\h);
                \\coordinate (B1) at (1.2,\\h-0.8);
                \\coordinate (C1) at (3,\\h);
                \\coordinate (M) at (3, \\h/2);
                \\draw[dashed] (A) -- (C);
                \\draw[dashed] (A) -- (M);
                \\draw (A) -- (B) -- (C) -- (C1) -- (B1) -- (A1) -- (A);
                \\draw (A1) -- (C1);
                \\draw (B) -- (B1);
                \\draw (B) -- (M);
                \\node[left] at (A) {$A$};
                \\node[below] at (B) {$B$};
                \\node[right] at (C) {$C$};
                \\node[left] at (A1) {$A'$};
                \\node[below] at (B1) {$B'$};
                \\node[right] at (C1) {$C'$};
                \\node[right] at (M) {$C_1$};
                \\draw[blue, fill=blue!20] (B) ++(0.3,0.2) arc (30:80:0.4);
            \\end{tikzpicture}
            \\end{center}''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + tikz_code + 
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

