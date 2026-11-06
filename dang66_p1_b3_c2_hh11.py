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


def bt_dang66_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Cập nhật hàm format_latex_frac để dùng hàm latex của sympy
            def format_latex_frac(val):
                # Dùng hàm latex của sympy để tự động xử lý số và biểu thức căn
                return latex(val)

            # ... (Giữ nguyên phần khai báo biến n và tính toán dist_coeff)
            n_choices = [Rational(1, 2), Rational(1), Rational(3, 2), Rational(2)]
            n = random.choice(n_choices)

            # Tính khoảng cách AK theo a: dist_coeff là biểu thức sympy
            val_ak = sqrt(3 * n**2 / (3 + 4 * n**2))
            dist_coeff = val_ak

            # Đáp án đúng tan(alpha) = n
            ans_correct = n

            # Tạo đáp án nhiễu
            def get_distractors(correct):
                s = set()
                options = [Rational(1, 4), Rational(1, 2), Rational(3, 4), Rational(1), Rational(3, 2), Rational(2)]
                while len(s) < 3:
                    val = random.choice(options)
                    if val != correct:
                        s.add(val)
                return list(s)

            wrong_answers = get_distractors(ans_correct)
            all_answers = [ans_correct] + wrong_answers
            random.shuffle(all_answers)

            # Chuỗi đáp án
            da_d = '\\True $' + format_latex_frac(ans_correct) + '$'
            da_s1 = '$' + format_latex_frac(all_answers[1]) + '$'
            da_s2 = '$' + format_latex_frac(all_answers[2]) + '$'
            da_s3 = '$' + format_latex_frac(all_answers[3]) + '$'
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # TikZ Figure
            tikz_fig = ('''\\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (2,-1.5);
            \\coordinate (C) at (4,0);
            \\coordinate (S) at (0,3);
            \\coordinate (M) at ($(B)!0.5!(C)$);
            \\draw (S) -- (B) -- (C) -- cycle;
            \\draw (S) -- (A) -- (B);
            \\draw[dashed] (A) -- (C);
            \\draw[dashed] (A) -- (M);
            \\draw (S) -- (M);
            \\draw[dashed] (A) -- ($(S)!(A)!(M)$) coordinate (K);
            \\node[left] at (A) {$A$};
            \\node[below] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[above] at (S) {$S$};
            \\node[below] at (M) {$M$};
            \\node[right] at (K) {$K$};
            \\end{tikzpicture}''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$ và $SA \\perp (ABC)$. Biết rằng khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ bằng $%s a$. $\\tan \\alpha$ với $\\alpha$ là góc tạo bởi giữa cạnh $SB$ và mặt phẳng $(ABC)$ bằng}
            {%s}''' % (format_latex_frac(dist_coeff), tikz_fig))

            # Lời giải
            # Sử dụng trực tiếp format_latex_frac (nay đã là latex(val)) để render công thức
            loigiai = ('''Gọi $M$ là trung điểm của $BC$, dựng $AK \\perp SM$ tại $K$ thì $AK \\perp (SBC)$, do đó $d(A,(SBC)) = AK = %s a$. \\\\
            Vì $ABC$ là tam giác đều cạnh $a$ nên $AM = \\frac{a\\sqrt{3}}{2}$. \\\\
            Trong tam giác vuông $SAM$ vuông tại $A$, có đường cao $AK$, ta có: \\\\
            $\\frac{1}{AK^2} = \\frac{1}{AM^2} + \\frac{1}{SA^2} \\\\
            \\Rightarrow \\frac{1}{SA^2} = \\frac{1}{AK^2} - \\frac{1}{AM^2} = \\frac{1}{(%s a)^2} - \\frac{1}{(\\frac{\\sqrt{3}}{2}a)^2} = \\frac{1}{%s a^2} - \\frac{4}{3a^2} = \\frac{1}{%s a^2} \\\\
            \\Rightarrow SA = %s a$. \\\\
            Góc tạo bởi giữa cạnh $SB$ và mặt phẳng $(ABC)$ là góc $\\widehat{SBA} = \\alpha$. \\\\
            Khi đó: $\\tan \\alpha = \\frac{SA}{AB} = \\frac{%s a}{a} = %s$.'''
            % (format_latex_frac(dist_coeff), 
               format_latex_frac(dist_coeff),
               latex(dist_coeff**2),
               latex(n**2), 
               format_latex_frac(n),
               format_latex_frac(n), 
               format_latex_frac(n)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+list_1[0]+'}\n'
                '{'+list_1[1]+'}\n'
                '{'+list_1[2]+'}\n'
                '{'+list_1[3]+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

