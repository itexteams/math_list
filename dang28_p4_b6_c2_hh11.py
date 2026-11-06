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


def bt_dang28_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # AB = k*a, BB' = h*a, AD = p*sqrt(q)*a
            # Để AB' đẹp, AB' = sqrt(k^2 + h^2)*a
            k = randint(1, 3) # Hệ số của AB
            h = randint(2, 4) # Hệ số của BB'
            p = randint(1, 2) # Hệ số ngoài căn của AD
            q = random.choice([2, 3, 5]) # Số trong căn của AD

            # Tính toán các giá trị
            val_AB = k * a
            val_AD = p * sqrt(q) * a
            val_BB_prime = h * a
            val_AB_prime_sq = k**2 + h**2
            val_AB_prime = sqrt(val_AB_prime_sq) * a

            # Diện tích đáy
            S_day = val_AB * val_AD # k * p * sqrt(q) * a^2
            # Thể tích
            V_dung = val_BB_prime * S_day # h * k * p * sqrt(q) * a^3

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            kq_dung = V_dung
            distractors = [
                (Rational(1, 3) * V_dung), # Công thức khối chóp
                (val_AB_prime * S_day),    # Nhầm chiều cao là đường chéo mặt bên
                (val_AB * val_AD),         # Quên nhân chiều cao (diện tích đáy)
                (2 * V_dung),              # Gấp đôi thể tích
                (sqrt(k**2 + p**2 * q) * val_BB_prime * a**2) # Nhầm đường chéo đáy
            ]

            # Lọc bỏ các giá trị trùng và chọn 3 đáp án sai
            s_list = []
            for d in distractors:
                if d != kq_dung and d not in s_list:
                    s_list.append(d)
            random.shuffle(s_list)
            das1, das2, das3 = s_list[0], s_list[1], s_list[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (
                "Cho hình lăng trụ đứng $ABCD.A'B'C'D'$ có đáy $ABCD$ là hình chữ nhật, "
                "$AB = %s$, $AD = %s$, $AB' = %s$. Tính thể tích khối lăng trụ đã cho."
                % (latex(val_AB), latex(val_AD), latex(val_AB_prime))
            )

            # --- Hình vẽ TikZ ---
            # Tọa độ các điểm để vẽ hình lăng trụ đứng
            # A(0,0), B(3,0), C(4.5,1), D(1.5,1)
            # Chiều cao h = 3.5
            tikz_code = r"""\begin{center} \begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, line width=1pt]
            \coordinate (A) at (0,0);
            \coordinate (B) at (3,0);
            \coordinate (C) at (4.2,1.2);
            \coordinate (D) at (1.2,1.2);
            \coordinate (A1) at (0,3.5);
            \coordinate (B1) at (3,3.5);
            \coordinate (C1) at (4.2,4.7);
            \coordinate (D1) at (1.2,4.7);
            \draw (A1)--(B1)--(C1)--(D1)--cycle;
            \draw (A)--(B)--(C);
            \draw [dashed] (C)--(D)--(A);
            \draw (A)--(A1) (B)--(B1) (C)--(C1);
            \draw [dashed] (D)--(D1);
            \draw (A)--(B1);
            \draw (D1)--(B1);
            \draw (D) node[below left]{$D$};
            \draw (A) node[below left]{$A$};
            \draw (B) node[below right]{$B$};
            \draw (C) node[right]{$C$};
            \draw (A1) node[above left]{$A'$};
            \draw (B1) node[above right]{$B'$};
            \draw (C1) node[above right]{$C'$};
            \draw (D1) node[above left]{$D'$};
            \draw (D) +(0.2,0) -- +(0.2,0.2) -- +(0,0.2);
            \end{tikzpicture} \end{center}"""

            # --- Lời giải chi tiết ---
            loigiai = (
                "Diện tích hình chữ nhật $ABCD$ là: \\\\ "
                "$S_{ABCD} = AB \\cdot AD = %s \\cdot %s = %s$. \\\\ "
                "Vì $ABCD.A'B'C'D'$ là hình lăng trụ đứng nên $BB' \\perp (ABCD) \\Rightarrow BB' \\perp AB$. \\\\ "
                "Xét tam giác $ABB'$ vuông tại $B$, ta có: \\\\ "
                "$BB' = \\sqrt{AB'^2 - AB^2} = \\sqrt{\\left(%s\\right)^2 - \\left(%s\\right)^2} = %s$. \\\\ "
                "Vậy thể tích khối lăng trụ đã cho là: \\\\ "
                "$V = S_{ABCD} \\cdot BB' = %s \\cdot %s = %s$."
                % (latex(val_AB), latex(val_AD), latex(S_day),
                   latex(val_AB_prime), latex(val_AB), latex(val_BB_prime),
                   latex(S_day), latex(val_BB_prime), latex(kq_dung))
            )

            # --- Xuất kết quả ---
            da_d = "\\True $" + latex(kq_dung) + "$"
            da_s1 = "$" + latex(das1) + "$"
            da_s2 = "$" + latex(das2) + "$"
            da_s3 = "$" + latex(das3) + "$"

            list_ans = [da_d, da_s1, da_s2, da_s3]
            shuffle(list_ans)

            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + noidungcauhoi + "\n"
                "\\loigiai{" + tikz_code+ loigiai + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

