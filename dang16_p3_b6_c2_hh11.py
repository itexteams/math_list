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


def bt_dang16_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số: cạnh hình vuông đáy là 2*k*a
                k = random.randint(1, 2)
                canh_day = 2 * k
                dien_tich_day_val = canh_day**2 

                # Random chiều cao h = SH / a.
                h_val = random.randint(1, 3)

                # Tính thể tích V = (4hk^2 / 3) * a^3
                tu_so_v = 4 * h_val * (k**2)
                v_latex = "\\frac{%s a^3}{3}" % (tu_so_v)

                # Tính HC = k*sqrt(5)a
                hc_val_numeric = k * math.sqrt(5)
                hc_latex = latex(simplify(k * sqrt(5))) # Giữ latex để trình bày lời giải

                # Tính tan(alpha) = SH / HC và làm tròn đến hàng phần chục
                tan_val = h_val / hc_val_numeric
                da_dung_latex = "{:.1f}".format(tan_val) # Kết quả số thập phân

                # Các đáp án sai (cũng làm tròn đến hàng phần chục)
                s1 = "{:.1f}".format(h_val / (k * math.sqrt(3)))
                s2 = "{:.1f}".format(h_val / (k * math.sqrt(7)))
                s3 = "{:.1f}".format(h_val / (k * math.sqrt(2)))
                s4 = "{:.1f}".format((h_val * 1.5) / (k * math.sqrt(5)))

                # Đảm bảo không trùng và loại bỏ đáp án đúng nếu lỡ trùng
                list_sai = list(set([s1, s2, s3, s4]))
                if da_dung_latex in list_sai:
                    list_sai.remove(da_dung_latex)
                while len(list_sai) < 3: # Đảm bảo đủ đáp án sai
                    list_sai.append("{:.1f}".format(tan_val + random.uniform(0.2, 0.5)))

                random.shuffle(list_sai)

                # Câu hỏi
                noidungcauhoi = (
                    "Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh bằng $%s a$. "
                    "Tam giác $SAB$ cân tại $S$ và nằm trong mặt phẳng vuông góc với đáy. "
                    "Biết thể tích khối chóp $S.ABCD$ bằng $%s$. "
                    "Gọi $\\alpha$ là góc giữa $SC$ và mặt đáy, giá trị $\\tan \\alpha$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                    % (latex(canh_day), v_latex)
                )

                # TikZ code
                tikz_code = (
                    "\\begin{center} \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line width=1pt]\n"
                    "\\coordinate (B) at (0,0);\n"
                    "\\coordinate (C) at (4,0);\n"
                    "\\coordinate (A) at (1.5,1.5);\n"
                    "\\coordinate (D) at (5.5,1.5);\n"
                    "\\coordinate (H) at ($(A)!0.5!(B)$);\n"
                    "\\coordinate (S) at ($(H)+(0,4)$);\n"
                    "\\draw (S)--(B)--(C)--(D)--(S)--(C);\n"
                    "\\draw[dashed] (S)--(A)--(D) (A)--(B) (S)--(H)--(C);\n"
                    "\\node[left] at (A) {$A$};\n"
                    "\\node[left] at (B) {$B$};\n"
                    "\\node[right] at (C) {$C$};\n"
                    "\\node[right] at (D) {$D$};\n"
                    "\\node[above] at (S) {$S$};\n"
                    "\\node[below left] at (H) {$H$};\n"
                    "\\draw (H)++(0.2,0.1) -- ++(0,0.2) -- ++(-0.2,0);\n" 
                    "\\path (B)--(C) node[midway, below] {$%s a$};\n"
                    "\\end{tikzpicture} \\end{center}" % (latex(canh_day))
                )

                # Nội dung lời giải
                loigiai = (
                    "Dựng $SH \\perp AB$. Do $(SAB) \\perp (ABCD)$ theo giao tuyến $AB$ nên $SH \\perp (ABCD) \\Rightarrow \\alpha = \\widehat{SCH}$. \\\\\n"
                    "Diện tích đáy $S_{ABCD} = \\left( %s a \\right)^2 = %s a^2$. \\\\\n"
                    "Ta có $V_{S.ABCD} = \\frac{1}{3} SH \\cdot S_{ABCD} \\Rightarrow \\frac{1}{3} SH \\cdot %s a^2 = \\frac{%s a^3}{3} \\Rightarrow SH = %s a$. \\\\\n"
                    "Do $\\Delta SAB$ cân tại $S$ nên $H$ là trung điểm của $AB \\Rightarrow BH = \\frac{%s a}{2} = %s a$. \\\\\n"
                    "Xét tam giác vuông $BHC$, ta có $HC = \\sqrt{BH^2 + BC^2} = \\sqrt{(%s a)^2 + (%s a)^2} = %s a$. \\\\\n"
                    "Vậy $\\tan \\alpha = \\tan \\widehat{SCH} = \\frac{SH}{HC} = \\frac{%s a}{%s a} \\approx %s$."
                    % (latex(canh_day), latex(dien_tich_day_val), 
                       latex(dien_tich_day_val), tu_so_v, h_val,
                       latex(canh_day), k,
                       k, canh_day, hc_latex,
                       h_val, hc_latex, da_dung_latex)
                )
                dapan='\\shortans[0]{$%s$}\n'%(str(da_dung_latex).replace('.', ','))

                # Đáp án
                da_d = "\\True $\\tan \\alpha = " + da_dung_latex + "$"
                da_s1 = "$\\tan \\alpha = " + list_sai[0] + "$"
                da_s2 = "$\\tan \\alpha = " + list_sai[1] + "$"
                da_s3 = "$\\tan \\alpha = " + list_sai[2] + "$"

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + tikz_code+ str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

