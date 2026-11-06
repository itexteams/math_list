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


def bt_dang13_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Sử dụng trực tiếp đối tượng SymPy thay vì chuỗi để tránh lỗi TypeError
            data_sets = [
                (1, sp.sqrt(2), 1, 30),          # AC=a, BC=a*sqrt(2), SA=a -> tan=1/sqrt(3) -> 30 độ
                (1, sp.sqrt(3), 2, 45),          # AC=a, BC=a*sqrt(3), SA=2a -> tan=1 -> 45 độ
                (1, 1, sp.sqrt(6), 60),          # AC=a, BC=a, SA=a*sqrt(6) -> tan=sqrt(3) -> 60 độ
                (1, sp.sqrt(5), sp.sqrt(2), 30), # AC=a, BC=a*sqrt(5) -> AB=a*sqrt(6), SA=a*sqrt(2) -> tan=1/sqrt(3) -> 30 độ
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            k_ac, k_bc, k_sa, answer_val = random.choice(data_sets)

            # Tính AB = sqrt(AC^2 + BC^2)
            ab_expr = sp.simplify(sp.sqrt(k_ac**2 + k_bc**2))

            # Chuẩn bị chuỗi hiển thị cho đề bài và lời giải
            def format_a(val):
                if val == 1: return "a"
                return latex(val) + "a"

            ac_text = format_a(k_ac)
            bc_text = format_a(k_bc)
            sa_text = format_a(k_sa)
            ab_text = format_a(ab_expr)

            # Tính giá trị tan (SA/AB)
            tan_val = sp.simplify(k_sa / ab_expr)
            tan_text = latex(tan_val)

            # Các phương án trắc nghiệm
            correct_ans = str(answer_val) + "^\\circ"
            options = ["30^\\circ", "45^\\circ", "60^\\circ", "90^\\circ"]
            if correct_ans not in options:
                options[0] = correct_ans
            random.shuffle(options)

            # Đánh dấu đáp án đúng
            list_1 = []
            for opt in options:
                if opt == correct_ans:
                    list_1.append("\\True $" + opt + "$")
                else:
                    list_1.append("$" + opt + "$")

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Cho hình chóp $S.ABC$ có đáy là tam giác vuông tại $C$, $AC = %s$, $BC = %s$, "
                "$SA$ vuông góc với mặt phẳng đáy và $SA = %s$. Tính góc giữa đường thẳng $SB$ và mặt phẳng đáy."
                % (ac_text, bc_text, sa_text)
            )



            # Lời giải chi tiết
            loigiai = ("""\\begin{center}
            \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (C) at (1.5,-1.5);
            \\coordinate (B) at (4,0);
            \\coordinate (S) at (0,3.5);
            \\draw[line width=1pt] (S)--(A)--(C)--(B)--(S)--(C);
            \\draw[dashed, line width=1pt] (A)--(B);
            \\draw[line width=1pt] (S) node[above]{$S$} (A) node[left]{$A$} (B) node[right]{$B$} (C) node[below]{$C$};
            \\tkzMarkRightAngle[size=0.3](A,C,B)
            \\tkzMarkRightAngle[size=0.3](S,A,B)
            \\end{tikzpicture}
            \\end{center}"""
                "Có $SA \\perp \\left(ABC \\right)$ nên $AB$ là hình chiếu vuông góc của $SB$ trên mặt phẳng $\\left(ABC \\right)$.\\\\ "
                "$\\Rightarrow \\left(SB, \\left(ABC \\right) \\right) = \\left(SB, AB \\right) = \\widehat{SBA}$.\\\\ "
                "Mặt khác, tam giác $ABC$ vuông tại $C$ nên $AB = \\sqrt{AC^2 + BC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$.\\\\ "
                "Khi đó $\\tan \\widehat{SBA} = \\frac{SA}{AB} = \\frac{%s}{%s} = %s$.\\\\ "
                "Do đó $\\widehat{SBA} = %s^\\circ$."
                % (ac_text, bc_text, ab_text, sa_text, ab_text, tan_text, answer_val)
            )

            # Xuất câu trắc nghiệm theo mẫu content
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' 
                + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

