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


def bt_dang28_p3_b6_c2_hh11(self):
            # --- B1: Khởi tạo các số nguyên để đảm bảo tính chính xác ---
            k = randint(2, 5)      # AB (độ dài nguyên)
            h = randint(3, 6)      # BB' (chiều cao nguyên)
            p = randint(1, 3)      # Hệ số của AD
            q = random.choice([2, 3, 5]) # Số trong căn của AD (AD = p*sqrt(q))

            # --- B2: Tính toán các giá trị (KHÔNG làm tròn ở bước này) ---
            val_AB = float(k)
            # AD giữ giá trị thực
            val_AD_real = p * math.sqrt(q)
            # AB' tính từ k và h (cạnh huyền tam giác vuông ABB')
            val_AB_prime_real = math.sqrt(k**2 + h**2)

            # Diện tích đáy thực tế
            S_day_real = val_AB * val_AD_real
            # Thể tích thực tế: V = AB * AD * BB'
            V_real = val_AB * val_AD_real * float(h)

            # --- B3: Chỉ làm tròn kết quả cuối cùng ---
            kq_dung = round(V_real, 1)

            # Chuẩn bị hiển thị LaTeX cho AD và AB'
            # AD hiển thị dưới dạng p√q để đề bài đẹp hơn, hoặc dùng số thập phân
            val_AD_display = f"{p}\\sqrt{{{q}}}" if p > 1 else f"\\sqrt{{{q}}}"
            # AB' thường là căn không đẹp, ta lấy 2 chữ số thập phân cho đề bài
            val_AB_prime_display = str(round(val_AB_prime_real, 2)).replace('.', ',')

            # --- B4: Tạo các phương án sai ---
            distractors = set()
            while len(distractors) < 3:
                # Các loại sai lầm phổ biến
                wrong1 = round(V_real / 3.0, 1) # Nhầm sang khối chóp
                wrong2 = round(S_day_real, 1)    # Quên nhân chiều cao
                wrong3 = round(val_AB_prime_real * S_day_real, 1) # Nhầm đường chéo làm chiều cao
                wrong4 = round(V_real + random.uniform(-5, 5), 1) # Sai số ngẫu nhiên

                for w in [wrong1, wrong2, wrong3, wrong4]:
                    if w != kq_dung and w > 0:
                        distractors.add(w)
                if len(distractors) < 3:
                    distractors.add(round(kq_dung + random.randint(1, 10), 1))

            s_list = list(distractors)
            random.shuffle(s_list)
            das1, das2, das3 = s_list[0], s_list[1], s_list[2]

            # --- B5: Nội dung câu hỏi ---
            noidungcauhoi = (
                "Cho hình lăng trụ đứng $ABCD.A'B'C'D'$ có đáy $ABCD$ là hình chữ nhật, "
                f"$AB = {k}$, $AD = {val_AD_display}$, $AB' = {val_AB_prime_display}$. "
                "Thể tích $V$ của khối lăng trụ đã cho bằng bao nhiêu? "
                "(Làm tròn kết quả đến hàng phần chục)."
            )

            # --- B6: Lời giải chi tiết (Sử dụng kết quả không làm tròn trung gian) ---
            # Tính BB' để trình bày lời giải
            loigiai = (
                f"Diện tích hình chữ nhật $ABCD$ là: \\\\ "
                f"$S_{{ABCD}} = AB \\cdot AD = {k} \\cdot {val_AD_display} = {p*k}\\sqrt{{{q}}} \\approx {round(S_day_real, 2)}$. \\\\ "
                f"Vì $ABCD.A'B'C'D'$ là hình lăng trụ đứng nên $BB' \\perp (ABCD) \\Rightarrow BB' \\perp AB$. \\\\ "
                f"Xét tam giác $ABB'$ vuông tại $B$, ta có: \\\\ "
                f"$BB' = \\sqrt{{AB'^2 - AB^2}} = \\sqrt{{{round(val_AB_prime_real, 2)}^2 - {k}^2}} \\approx {h}$. \\\\ "
                f"Vậy thể tích khối lăng trụ đã cho là: \\\\ "
                f"$V = S_{{ABCD}} \\cdot BB' = {p*k}\\sqrt{{{q}}} \\cdot {h} = {p*k*h}\\sqrt{{{q}}} \\approx {str(kq_dung).replace('.', ',')} $."
            )

            # --- B7: Xuất kết quả ---
            tikz_code = r"""\begin{center} \begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, line width=0.8pt, scale=0.7]
            \coordinate (A) at (0,0); \coordinate (B) at (3,0); \coordinate (C) at (4.2,1.2); \coordinate (D) at (1.2,1.2);
            \coordinate (A1) at (0,3.5); \coordinate (B1) at (3,3.5); \coordinate (C1) at (4.2,4.7); \coordinate (D1) at (1.2,4.7);
            \draw (A1)--(B1)--(C1)--(D1)--cycle; \draw (A)--(B)--(C); \draw [dashed] (C)--(D)--(A);
            \draw (A)--(A1) (B)--(B1) (C)--(C1); \draw [dashed] (D)--(D1); \draw (A)--(B1);
            \draw (D) node[below left]{$D$}; \draw (A) node[below left]{$A$}; \draw (B) node[below right]{$B$}; \draw (C) node[right]{$C$};
            \draw (A1) node[above left]{$A'$}; \draw (B1) node[above right]{$B'$}; \draw (C1) node[above right]{$C'$}; \draw (D1) node[above left]{$D'$};
            \end{tikzpicture} \end{center}"""

            da_d = "\\True $" + str(kq_dung).replace('.', ',') + "$"
            da_s1 = "$" + str(das1).replace('.', ',') + "$"
            da_s2 = "$" + str(das2).replace('.', ',') + "$"
            da_s3 = "$" + str(das3).replace('.', ',') + "$"

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + noidungcauhoi + "\n"
                "\\choice\n"
                "{" + list_ans[0] + "}\n"
                "{" + list_ans[1] + "}\n"
                "{" + list_ans[2] + "}\n"
                "{" + list_ans[3] + "}\n"
                "\\loigiai{" + tikz_code + loigiai + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

