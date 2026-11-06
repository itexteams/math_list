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


def bt_dang29_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Cạnh đáy là a * sqrt(n)
            m = random.randint(1, 3)
            n = 6 * (m**2)
            canh_day_hien_thi = latex(sqrt(n))

            # Góc giữa cạnh bên và mặt đáy (mặc định 60 độ để giống đề mẫu)
            goc = 60
            goc_rad = pi / 3

            # 1. Tính diện tích đáy ABCD
            # S_ABCD = (a*sqrt(n))^2 = n*a^2
            s_abcd_val = n

            # 2. Tính độ dài nửa đường chéo DO
            # BD = canh * sqrt(2) = a * sqrt(2n)
            # DO = 1/2 * BD = a * sqrt(2n) / 2
            do_val_sq = (2 * n) / 4 # Đây là hệ số của a^2 cho DO^2
            do_latex = latex(sqrt(n * 2) / 2)

            # 3. Tính chiều cao SO
            # SO = DO * tan(60) = DO * sqrt(3)
            so_val_hieu_chinh = (sqrt(n * 2) / 2) * sqrt(3)
            so_latex = latex(so_val_hieu_chinh)

            # 4. Tính thể tích khối chóp S.ABCD
            # V_SABCD = 1/3 * SO * S_ABCD
            v_sabcd_hieu_chinh = (1/3) * so_val_hieu_chinh * s_abcd_val
            v_sabcd_val = int(v_sabcd_hieu_chinh) # Với n=6*m^2, kết quả luôn là 6*m^3

            # 5. Tính thể tích khối chóp S.ABC (Yêu cầu đề bài)
            # V_SABC = 1/2 * V_SABCD
            v_correct = v_sabcd_val // 2

            # Tạo các phương án sai
            phuong_an_sai = {v_sabcd_val, v_correct * 2, v_correct + 2, v_correct + 3, v_correct - 1}
            if v_correct in phuong_an_sai:
                phuong_an_sai.remove(v_correct)
            list_sai = random.sample(list(phuong_an_sai), 3)

            # Đáp án
            da_d = "\\True $V = " + str(v_correct) + "a^3$"
            da_s1 = "$V = " + str(list_sai[0]) + "a^3$"
            da_s2 = "$V = " + str(list_sai[1]) + "a^3$"
            da_s3 = "$V = " + str(list_sai[2]) + "a^3$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $a\\sqrt{" + str(n) + "}$, "
                "góc giữa cạnh bên và mặt đáy bằng $" + str(goc) + "^{\\circ}$. "
                "Thể tích $V$ của khối chóp $S.ABC$ bằng"
            )

            # Hình vẽ TikZ
            hinh_ve = r"""\begin{center}
            \begin{tikzpicture}[scale=0.8, line width=1pt, line join=round, line cap=round]
                \coordinate (A) at (1.5,1.5);
                \coordinate (B) at (0,0);
                \coordinate (C) at (4,0);
                \coordinate (D) at (5.5,1.5);
                \coordinate (O) at (2.75,0.75);
                \coordinate (S) at (2.75,5);
                \draw [dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O);
                \draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);
                \node at (A) [left] {$A$};
                \node at (B) [below left] {$B$};
                \node at (C) [below right] {$C$};
                \node at (D) [right] {$D$};
                \node at (S) [above] {$S$};
                \node at (O) [below] {$O$};
            \end{tikzpicture}
            \end{center}"""

            # Lời giải chi tiết
            loigiai = (
                "Diện tích đáy là: $S_{ABCD} = AB^2 = \\left( a\\sqrt{" + str(n) + "} \\right)^2 = " + str(s_abcd_val) + "a^2$. \\\\"
                "Góc giữa cạnh bên $SD$ và mặt đáy $(ABCD)$ là $\\widehat{\\left( SD, (ABCD) \\right)} = \\widehat{SDO} \\Rightarrow \\widehat{SDO} = " + str(goc) + "^{\\circ}$. \\\\"
                "$ABCD$ là hình vuông suy ra $DO = \\frac{1}{2}BD = \\frac{1}{2}AB\\sqrt{2} = \\frac{1}{2}a\\sqrt{" + str(n) + "}\\cdot\\sqrt{2} = " + do_latex + "a$. \\\\"
                "Xét tam giác vuông $SOD$: $SO = DO \\cdot \\tan \\widehat{SDO} = " + do_latex + "a \\cdot \\tan " + str(goc) + "^{\\circ} = " + so_latex + "a$. \\\\"
                "Thể tích khối chóp $S.ABCD$ là $V_{S.ABCD} = \\frac{1}{3} \\cdot SO \\cdot S_{ABCD} = \\frac{1}{3} \\cdot " + so_latex + "a \\cdot " + str(s_abcd_val) + "a^2 = " + str(v_sabcd_val) + "a^3$. \\\\"
                "Vậy thể tích khối chóp $S.ABC$ bằng $V = \\frac{1}{2} V_{S.ABCD} = \\frac{1}{2} \\cdot " + str(v_sabcd_val) + "a^3 = " + str(v_correct) + "a^3$."
            )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + 
                '\\choice \n'
                '{' + list_1[0] + '}\n'
                '{' + list_1[1] + '}\n'
                '{' + list_1[2] + '}\n'
                '{' + list_1[3] + '}\n'
                '\\loigiai{' + hinh_ve+ loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

