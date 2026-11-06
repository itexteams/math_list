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


def bt_dang63_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến và hằng số
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Chọn k để SA chia hết cho 3 giúp SM = 1/3 SC ra số nguyên/đẹp
                k = random.randint(2, 4)
                sa_val = 3 * k  # Ví dụ: 6, 9, 12...
                # AB phải thỏa mãn bất đẳng thức tam giác mặt bên: AB < 2*SA
                ab_val = random.randint(k + 1, 2 * k - 1) * 2 # Đảm bảo số chẵn cho đẹp

                # Tính toán các giá trị hình học bằng Sympy
                SA_sym = sa_val
                AB_sym = ab_val
                # Vì chóp tam giác đều nên các cạnh bên bằng nhau
                SB_sym = SA_sym
                SC_sym = SA_sym
                # SM = 1/2 MC => SM = 1/3 SC
                SM_sym = Rational(1, 3) * SC_sym

                # 1. Tính cos góc ở đỉnh mặt bên (cos ASB = cos ASC = cos BSC)
                # cos(ASB) = (SA^2 + SB^2 - AB^2) / (2 * SA * SB)
                cos_phi = Rational(SA_sym**2 + SB_sym**2 - AB_sym**2, 2 * SA_sym * SB_sym)

                # 2. Tính độ dài AM bằng định lý hàm cos trong tam giác SAM
                am_sq = SA_sym**2 + SM_sym**2 - 2 * SA_sym * SM_sym * cos_phi
                am_val = simplify(sqrt(am_sq))

                # 3. Tính tích vô hướng AM.SB bằng vector
                # AM = SM - SA (vector)
                # AM.SB = (1/3 SC - SA).SB = 1/3 SC.SB.cos(CSB) - SA.SB.cos(ASB)
                dot_product = Rational(1, 3) * SC_sym * SB_sym * cos_phi - SA_sym * SB_sym * cos_phi
                abs_dot = abs(dot_product)

                # 4. Tính cos(AM, SB) = |AM.SB| / (AM * SB)
                cos_final = simplify(abs_dot / (am_val * SB_sym))

                # Bước 4: Điều chỉnh các phương án
                # Đáp án đúng
                da = '$%s$' % (latex(cos_final))

                # Tạo các phương án sai
                s = [
                    '$%s$' % (latex(simplify(cos_final * Rational(1, 2)))),
                    '$%s$' % (latex(simplify(Rational(1, 2)))),
                    '$%s$' % (latex(simplify(abs_dot / (SA_sym * SB_sym)))),
                    '$%s$' % (latex(simplify(cos_phi))),
                    '$%s$' % (latex(simplify(sqrt(am_sq) / (2 * SA_sym))))
                ]

                # Lọc bỏ đáp án trùng với đáp án đúng
                s = [x for x in s if x != da]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp đều $S.ABC$ có $SA = %sa, AB = %sa$. Gọi $M$ là điểm thuộc cạnh $SC$ sao cho '
                    '$SM = \\frac{1}{2} MC$. Tính cosin của góc giữa hai đường thẳng $SB$ và $AM$.'
                    % (latex(sa_val), latex(ab_val))
                )

                # Hình vẽ TikZ
                tikz_code = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]\n'
                    '    \\coordinate (A) at (0,0);\n'
                    '    \\coordinate (B) at (1.2,-1.2);\n'
                    '    \\coordinate (C) at (3.5,0);\n'
                    '    \\coordinate (S) at (1.6, 3.5);\n'
                    '    \\coordinate (M) at ($(S)!0.33!(C)$);\n'
                    '    \\draw[dashed] (A) -- (C);\n'
                    '    \\draw (A) -- (B) -- (C);\n'
                    '    \\draw (S) -- (A) (S) -- (B) (S) -- (C);\n'
                    '    \\draw[dashed] (A) -- (M);\n'
                    '    \\node[left] at (A) {$A$};\n'
                    '    \\node[below] at (B) {$B$};\n'
                    '    \\node[right] at (C) {$C$};\n'
                    '    \\node[above] at (S) {$S$};\n'
                    '    \\node[above right] at (M) {$M$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Ta có $\\cos \\widehat{ASB} = \\frac{SA^2 + SB^2 - AB^2}{2SA \\cdot SB} = \\frac{(%sa)^2 + (%sa)^2 - (%sa)^2}{2 \\cdot %sa \\cdot %sa} = %s$. \\\\'
                    'Vì $S.ABC$ là hình chóp đều nên $\\cos \\widehat{CSB} = \\cos \\widehat{ASC} = \\cos \\widehat{ASB} = %s$. \\\\'
                    'Từ giả thiết $SM = \\frac{1}{2} MC \\Rightarrow SM = \\frac{1}{3} SC = %sa$. \\\\'
                    'Xét tam giác $SAM$, ta có: \\\\'
                    '$AM^2 = SA^2 + SM^2 - 2SA \\cdot SM \\cdot \\cos \\widehat{ASC} = (%sa)^2 + (%sa)^2 - 2 \\cdot %sa \\cdot %sa \\cdot %s = %sa^2$. \\\\'
                    '$\\Rightarrow AM = %sa$. \\\\'
                    'Ta có: $\\vec{AM} \\cdot \\vec{SB} = (\\vec{SM} - \\vec{SA}) \\cdot \\vec{SB} = \\vec{SM} \\cdot \\vec{SB} - \\vec{SA} \\cdot \\vec{SB}$ \\\\'
                    '$= SM \\cdot SB \\cdot \\cos \\widehat{BSC} - SA \\cdot SB \\cdot \\cos \\widehat{ASB}$ \\\\'
                    '$= %sa \\cdot %sa \\cdot %s - %sa \\cdot %sa \\cdot %s = %sa^2$. \\\\'
                    'Cosin góc giữa hai đường thẳng $AM$ và $SB$ là: \\\\'
                    '$\\cos(AM, SB) = \\frac{|\\vec{AM} \\cdot \\vec{SB}|}{AM \\cdot SB} = \\frac{|%sa^2|}{%sa \\cdot %sa} = %s$.'
                    % (latex(sa_val), latex(sa_val), latex(ab_val), latex(sa_val), latex(sa_val), latex(cos_phi),
                       latex(cos_phi), latex(SM_sym),
                       latex(sa_val), latex(SM_sym), latex(sa_val), latex(SM_sym), latex(cos_phi), latex(am_sq),
                       latex(am_val),
                       latex(SM_sym), latex(sa_val), latex(cos_phi), latex(sa_val), latex(sa_val), latex(cos_phi), latex(abs(dot_product)),
                       latex(abs(dot_product)), latex(am_val), latex(sa_val), latex(cos_final))
                )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{'+ tikz_code+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

