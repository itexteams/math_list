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


def bt_dang32_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu
            a = symbols('a')

            # B3: Suy nghĩ tìm cách random bài toán
            # Chúng ta sẽ thay đổi hệ số k trong SA = a*sqrt(k)
            # Để góc ra số đẹp (30, 45, 60), ta chọn các giá trị k phù hợp
            # k=2 => tan = 1/sqrt(3) => 30 độ
            # k=0.5 (không nguyên) => tan = 1/sqrt(1.5) => không đẹp
            # Để giữ nguyên bản chất bài toán như ảnh mẫu, ta có thể random cạnh đáy 'a' hoặc giữ nguyên hệ số k=2
            # Ở đây tôi sẽ giữ k=2 để đảm bảo góc 30 độ như đề bài gốc nhưng có thể mở rộng danh sách đáp án nhiễu

            list_k = [2] # Có thể thêm các giá trị khác nếu muốn bài toán khác đi
            k_val = random.choice(list_k)

            # Tính toán các giá trị
            sa_latex = "a\\sqrt{%s}" % k_val if k_val != 1 else "a"
            # SB^2 = SA^2 + AB^2 = k*a^2 + a^2 = (k+1)a^2
            sb_sq = k_val + 1
            sb_latex = "a\\sqrt{%s}" % sb_sq

            # Góc CSB: tan(CSB) = BC / SB = a / (a*sqrt(sb_sq)) = 1/sqrt(sb_sq)
            # Với k=2, sb_sq = 3, tan = 1/sqrt(3) => angle = 30
            angle_correct = 30

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            options = {30, 45, 60, 90}
            da_d = "\\True $%s^\\circ$" % angle_correct

            wrong_options = list(options - {angle_correct})
            random.shuffle(wrong_options)

            da_s1 = "$%s^\\circ$" % wrong_options[0]
            da_s2 = "$%s^\\circ$" % wrong_options[1]
            da_s3 = "$%s^\\circ$" % wrong_options[2]

            # Trộn thứ tự đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, cạnh bên $SA$ vuông góc với mặt đáy và $SA = %s$. "
                "Tính góc giữa đường thẳng $SC$ và mặt phẳng $\\left(SAB\\right)$."
                % sa_latex
            )

            # Vẽ hình TikZ
            tikz_code = r"""\begin{center} \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, line width=1pt]
                \coordinate (A) at (0,0);
                \coordinate (B) at (-1.2,-1);
                \coordinate (D) at (2.5,0);
                \coordinate (C) at ($(B)+(D)-(A)$);
                \coordinate (S) at (0,2.5);
                \draw (S)--(B)--(C)--(D)--(S)--(C);
                \draw [dashed] (S)--(A)--(B) (A)--(D);
                \node at (A) [left] {$A$};
                \node at (B) [left] {$B$};
                \node at (C) [right] {$C$};
                \node at (D) [right] {$D$};
                \node at (S) [above] {$S$};
            \end{tikzpicture} \end{center}"""

            # B2: Viết lại lời giải chi tiết
            loigiai = (
                "Ta có $CB \\perp AB$ (do $ABCD$ là hình vuông) và $CB \\perp SA$ (do $SA \\perp \\left(ABCD\\right)$). \\\\"
                "Suy ra $CB \\perp \\left(SAB\\right)$. \\\\"
                "Khi đó $SB$ là hình chiếu vuông góc của $SC$ lên mặt phẳng $\\left(SAB\\right)$. \\\\"
                "Vậy góc giữa đường thẳng $SC$ và mặt phẳng $\\left(SAB\\right)$ là góc $\\widehat{CSB}$. \\\\"
                "Xét tam giác $SAB$ vuông tại $A$, ta có $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{\\left(%s\\right)^2 + a^2} = %s$. \\\\"
                "Xét tam giác $CSB$ vuông tại $B$, ta có $\\tan \\widehat{CSB} = \\frac{CB}{SB} = \\frac{a}{%s} = \\frac{1}{\\sqrt{3}}$. \\\\"
                "Vậy $\\widehat{CSB} = 30^\\circ$."
                % (sa_latex, sb_latex, sb_latex)
            )

            # B1 & Content: Xuất theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + tikz_code+ loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

