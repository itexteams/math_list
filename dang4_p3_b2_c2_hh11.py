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


def bt_dang4_p3_b2_c2_hh11(self):
            # Khai báo biến
            # Để diện tích là số hữu tỉ đẹp, ta chọn các cạnh là số chẵn
            list_a = [8, 10, 12, 14] # Đáy lớn AD
            list_b = [4, 6, 8]       # Đáy nhỏ BC (b < a)
            list_h = [6, 8, 10]      # Chiều cao SA

            a = random.choice(list_a)
            b = random.choice([x for x in list_b if x < a])
            h = random.choice(list_h)

            # B2: Tính toán lời giải
            # MQ = SA/2
            mq_val = Rational(h, 2)
            # MN là đường trung bình hình thang ABCD: MN = (AD + BC)/2
            mn_val = Rational(a + b, 2)
            # QP là đường trung bình tam giác SBC (hoặc tính qua tỉ lệ song song): QP = BC/2
            qp_val = Rational(b, 2)

            # Diện tích hình thang vuông MNPQ: S = (MN + QP) * MQ / 2
            dien_tich = Rational((mn_val + qp_val) * mq_val, 2)

            # Chuyển đổi sang định dạng số thập phân dùng dấu phẩy cho tiếng Việt
            def format_num(n):
                return str(float(n)).replace('.', ',').rstrip('0').rstrip(',') if n % 1 != 0 else str(int(n))

            kq_chuan = format_num(dien_tich)

            # B4: Tạo các phương án sai không trùng đáp án đúng
            sai_1 = format_num(dien_tich + random.choice([1, 2, 5]))
            sai_2 = format_num(dien_tich - random.choice([1, 2]))
            if float(dien_tich) <= 2: sai_2 = format_num(dien_tich + 3)
            sai_3 = format_num(Rational((a + b) * h, 4)) # Tính nhầm công thức khác

            options = [
                '\\True $' + kq_chuan + '$',
                '$' + sai_1 + '$',
                '$' + sai_2 + '$',
                '$' + sai_3 + '$'
            ]
            random.shuffle(options)

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Cho hình chóp $S.ABCD$ với đáy $ABCD$ là hình thang vuông tại $A$, đáy lớn $AD = " + str(a) + "$, "
                "đáy nhỏ $BC = " + str(b) + "$. $SA$ vuông góc với đáy, $SA = " + str(h) + "$. Gọi $M$ là trung điểm của $AB$. "
                "$(P)$ là mặt phẳng qua $M$ và vuông góc với $AB$. Giao tuyến của mặt phẳng $(P)$ với các mặt của hình chóp $S.ABCD$ có diện tích bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)."
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                "Vì $ABCD$ là hình thang vuông tại $A$ nên $AD \\perp AB$ và $BC \\perp AB$.\\\\ "
                "Ta có $SA \\perp (ABCD) \\Rightarrow SA \\perp AB$.\\\\ "
                "Mặt phẳng $(P) \\perp AB$ tại $M$, mà $SA, AD, BC$ đều vuông góc với $AB$, do đó $(P)$ song song với các đường thẳng $SA, AD, BC$.\\\\ "
                "Trong mặt phẳng $(ABCD)$, qua $M$ kẻ đường thẳng song song với $AD$ cắt $CD$ tại $N$. Vì $M$ là trung điểm $AB$ và $MN // AD // BC$ nên $N$ là trung điểm $CD$ và $MN = \\frac{AD+BC}{2} = \\frac{" + str(a) + "+" + str(b) + "}{2} = " + format_num(mn_val) + "$.\\\\ "
                "Trong mặt phẳng $(SAB)$, qua $M$ kẻ đường thẳng song song với $SA$ cắt $SB$ tại $Q$. Vì $M$ là trung điểm $AB$ nên $Q$ là trung điểm $SB$ và $MQ = \\frac{SA}{2} = \\frac{" + str(h) + "}{2} = " + format_num(mq_val) + "$.\\\\ "
                "Trong mặt phẳng $(SBC)$, qua $Q$ kẻ đường thẳng song song với $BC$ cắt $SC$ tại $P$. Vì $Q$ là trung điểm $SB$ nên $P$ là trung điểm $SC$ và $QP = \\frac{BC}{2} = \\frac{" + str(b) + "}{2} = " + format_num(qp_val) + "$.\\\\ "
                "Thiết diện là hình thang $MNPQ$. Do $MQ // SA$ và $SA \\perp (ABCD)$ nên $MQ \\perp (ABCD)$, suy ra $MQ \\perp MN$.\\\\ "
                "Vậy thiết diện $MNPQ$ là hình thang vuông tại $M$ và $Q$.\\\\ "
                "Diện tích thiết diện là: $S = \\frac{\\left(MN + QP \\right) \\cdot MQ}{2} = \\frac{\\left(" + format_num(mn_val) + " + " + format_num(qp_val) + "\\right) \\cdot " + format_num(mq_val) + "}{2} = " + kq_chuan + "$."
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq_chuan)
            # TikZ code vẽ hình
            tikz_code = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[scale=0.6, line width=1pt, line join=round, line cap=round]\n"
                "\\coordinate (A) at (0,0); \\coordinate (B) at (2,-2); \\coordinate (C) at (7,-2); \\coordinate (D) at (6,0); \\coordinate (S) at (0,5);\n"
                "\\coordinate (M) at ($(A)!0.5!(B)$); \\coordinate (N) at ($(D)!0.5!(C)$); \n"
                "\\coordinate (Q) at ($(S)!0.5!(B)$); \\coordinate (P) at ($(S)!0.5!(C)$);\n"
                "\\draw (S)--(B)--(C)--(D)--(S) (S)--(C) (Q)--(P) (A)--(S) (A)--(B) (M)--(Q) (N)--(P);\n"
                "\\draw[dashed]  (A)--(D) (M)--(N) ;\n"
                "\\foreach \\p/\\pos in {S/above, A/left, B/below, C/right, D/right, M/left, N/right, Q/left, P/right} \\fill (\\p) node[\\pos] {$\\p$};\n"
                "\\end{tikzpicture}\n"
                "\\end{center}"
            )

            # Xuất nội dung theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

