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


def bt_dang42_p3_b1_c2_hh11(self):
            # Khai báo biến
            # để phần tính toán trong lời giải sinh động hơn.

            a_val = random.randint(2, 10)
            a = symbols('a')

            # Các thông số tính toán dựa trên a
            # NJ = a*sqrt(3)/2
            nj_sq = Rational(3, 4) * a_val**2
            nc_sq = 2 * a_val**2
            jc_sq = Rational(5, 4) * a_val**2

            # cos(JNC) = (NJ^2 + NC^2 - JC^2) / (2 * NJ * NC)
            # Kết quả rút gọn luôn là sqrt(6)/4
            kq_chuan = "\\frac{\\sqrt{6}}{4}"

            # B4-Điều chỉnh các phương án sai không trùng đáp án đúng
            list_options = [
                "\\frac{\\sqrt{6}}{4}", # Đáp án đúng
                "\\frac{\\sqrt{6}}{2}",
                "\\frac{\\sqrt{10}}{4}",
                "\\frac{\\sqrt{15}}{5}"
            ]

            # Trộn đáp án
            da_dung = "\\True $" + list_options[0] + "$"
            list_ans = [da_dung]
            for i in range(1, 4):
                list_ans.append("$" + list_options[i] + "$")

            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho lăng trụ tam giác đều $ABC.MNP$ có tất cả các cạnh bằng nhau. Gọi $I$ là trung điểm cạnh $AC$. Cosin của góc giữa hai đường thẳng $NC$ và $IB$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).")

            # Hình vẽ TikZ
            hinh_ve = ("\\begin{center}\n"
                       "\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]\n"
                       "\\coordinate (A) at (0,0);\n"
                       "\\coordinate (C) at (1.5,-1.2);\n"
                       "\\coordinate (B) at (4,0);\n"
                       "\\coordinate (M) at (0,4);\n"
                       "\\coordinate (P) at (1.5,2.8);\n"
                       "\\coordinate (N) at (4,4);\n"
                       "\\coordinate (I) at ($(A)!0.5!(C)$);\n"
                       "\\coordinate (J) at ($(M)!0.5!(P)$);\n"
                       "\\draw (M)--(N)--(P)--cycle (N)--(B)--(C)--(P) (A)--(C);\n"
                       "\\draw[dashed] (A)--(B)  (I)--(B) ;\n"
                       "\\draw (M)--(A) (N)--(C) (N)--(J) (J)--(C) (I)--(J);\n"
                       "\\foreach \\p/\\pos in {A/left, B/right, C/below, M/above, N/above, P/right, I/below, J/left}\n"
                       "\\fill (\\p) node[\\pos] {$\\p$};\n"
                       "\\end{tikzpicture}\n"
                       "\\end{center}")

            # Lời giải chi tiết
            h1=sqrt(6)/4
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            loigiai = (hinh_ve + 
                       "Giả sử tất cả các cạnh của lăng trụ bằng $a=" + str(a_val) + "$. \\\\ \n"
                       "Gọi $J$ là trung điểm của $MP$. Khi đó $NJ \\parallel IB$ và $NJ = IB$. \\\\ \n"
                       "Góc giữa hai đường thẳng $NC$ và $IB$ bằng góc giữa hai đường thẳng $NC$ và $NJ$, đó là $\\widehat{JNC}$ (hoặc góc bù của nó). \\\\ \n"
                       "Ta có: \\\\ \n"
                       "$NJ = \\frac{a\\sqrt{3}}{2} = \\frac{" + str(a_val) + "\\sqrt{3}}{2}$. \\\\ \n"
                       "$NC^2 = NB^2 + BC^2 = a^2 + a^2 = 2a^2 = " + str(nc_sq) + "$. \\\\ \n"
                       "$JC^2 = JI^2 + IC^2 = a^2 + (\\frac{a}{2})^2 = \\frac{5a^2}{4} = " + str(jc_sq) + "$. \\\\ \n"
                       "Xét tam giác $NJC$, áp dụng hệ quả định lý cosin: \\\\ \n"
                       "$\\cos \\widehat{JNC} = \\frac{NJ^2 + NC^2 - JC^2}{2 \\cdot NJ \\cdot NC} = \\frac{\\frac{3a^2}{4} + 2a^2 - \\frac{5a^2}{4}}{2 \\cdot \\frac{a\\sqrt{3}}{2} \\cdot a\\sqrt{2}} = \\frac{\\sqrt{6}}{4}$. \\\\ \n"
                       "Vì $\\frac{\\sqrt{6}}{4} > 0$ nên góc $\\widehat{JNC}$ là góc nhọn, vậy cosin cần tìm là $\\frac{\\sqrt{6}}{4} \\approx %s$."%(str(kqz)))

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))
            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

