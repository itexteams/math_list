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


def bt_dang64_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu cho SymPy
            a = symbols('a')

            # Danh sách các bộ dữ liệu (SA_coeff, AB_coeff, BC_coeff)
            data_sets = [
                (1, 1, sqrt(3)),
                (2, 1, sqrt(3)),
                (1, 1, 1),
                (sqrt(2), 1, 1),
                (2, 2, 2*sqrt(3))
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            sa_c, ab_c, bc_c = random.choice(data_sets)

            # Tính toán các đại lượng bằng SymPy
            ac_sq = (ab_c * a)**2 + (bc_c * a)**2
            ac = sqrt(ac_sq)
            bd = ac
            bo = bd / 2
            sc_sq = (sa_c * a)**2 + ac_sq
            sc = sqrt(sc_sq)
            om = sc / 2
            am = (sa_c * a) / 2
            bm_sq = am**2 + (ab_c * a)**2
            bm = sqrt(bm_sq)

            # Tính cos(MOB)
            cos_val = (om**2 + bo**2 - bm_sq) / (2 * om * bo)
            cos_val = sp.simplify(abs(cos_val))

            # Đáp án
            da_dung = '$%s$' % (latex(cos_val))
            potential_distractors = [
                sp.simplify(cos_val * 2), sp.simplify(cos_val / 2),
                sqrt(3)/3, sqrt(2)/2, Rational(1, 2), sqrt(6)/6, sqrt(10)/10
            ]
            s = []
            for p in potential_distractors:
                latex_p = '$%s$' % (latex(p))
                if latex_p != da_dung and latex_p not in s:
                    s.append(latex_p)
            random.shuffle(s)
            list_1 = ['\\True ' + str(da_dung), s[0], s[1], s[2]]
            random.shuffle(list_1)

            # --- Mã TikZ vẽ hình ---
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]
                % Định nghĩa các điểm
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1.5,-1.2);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (S) at (0,3.5);
                \\coordinate (O) at ($(A)!0.5!(C)$);
                \\coordinate (M) at ($(S)!0.5!(A)$);
                \\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (O)--(M) (B)--(M);
                \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);
                \\node [left] at (A) {$A$};
                \\node [below left] at (B) {$B$};
                \\node [below right] at (C) {$C$};
                \\node [right] at (D) {$D$};
                \\node [above] at (S) {$S$};
                \\node [below] at (O) {$O$};
                \\node [left] at (M) {$M$};
                \\draw (0.3,0)--(0.3,0.3)--(0,0.3);
            \\end{tikzpicture}
            \\end{center}''')

            # --- Nội dung câu hỏi ---
            sa_text = latex(sa_c * a)
            ab_text = latex(ab_c * a)
            bc_text = latex(bc_c * a)

            noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, $SA \\perp (ABCD)$, $SA = %s$, $AB = %s$, $BC = %s$. Tính cosin của góc tạo bởi hai đường thẳng $SC$ và $BD$.'
                             % (sa_text, ab_text, bc_text))

            # --- Nội dung lời giải ---
            loigiai = ('''%s
                         Gọi $O$ là tâm của hình chữ nhật $ABCD$ và $M$ là trung điểm của $SA$.\\\\
                         Khi đó $OM$ là đường trung bình của tam giác $SAC$, suy ra $OM \\parallel SC$.\\\\
                         Do đó $(SC, BD) = (OM, BD)$. Ta tính các cạnh của tam giác $MOB$.\\\\
                         Ta có:\\\\
                         $AC = BD = \\sqrt{AB^2 + BC^2} = \\sqrt{(%s)^2 + (%s)^2} = %s$.\\\\
                         $BO = \\frac{BD}{2} = %s$.\\\\
                         $SC = \\sqrt{SA^2 + AC^2} = \\sqrt{(%s)^2 + (%s)^2} = %s \\Rightarrow OM = \\frac{SC}{2} = %s$.\\\\
                         Trong tam giác $MAB$ vuông tại $A$:\\\\
                         $BM = \\sqrt{AM^2 + AB^2} = \\sqrt{\\left(\\frac{%s}{2}\\right)^2 + (%s)^2} = %s$.\\\\
                         Áp dụng định lý hàm số cos trong tam giác $MOB$:\\\\
                         $\\cos \\widehat{MOB} = \\frac{OM^2 + BO^2 - BM^2}{2 \\cdot OM \\cdot BO} = \\frac{(%s)^2 + (%s)^2 - (%s)^2}{2 \\cdot %s \\cdot %s} = %s$.\\\\
                         Vậy $\\cos(SC, BD) = |\\cos \\widehat{MOB}| = %s$.'''
                       % (tikz_code, ab_text, bc_text, latex(ac), 
                          latex(bo), sa_text, latex(ac), latex(sc), latex(om),
                          sa_text, ab_text, latex(bm),
                          latex(om), latex(bo), latex(bm), latex(om), latex(bo), latex(cos_val),
                          latex(cos_val)
                         ))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

