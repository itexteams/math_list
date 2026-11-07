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


def bt_dang97_p1_b3_c1_ds11(self):
        # Khai báo biến & RANDOM ĐỐI SỐ
        a = random.randint(20, 35)    # nhiệt độ trung bình
        b = random.randint(2, 6)      # biên độ dao động
        t0 = random.randint(6, 11)    # giờ nhiệt độ trung bình
        
        # Giá trị min/max và thời điểm đạt được
        h_min = a - b
        h_max = a + b
        t_min = (t0 - 6) % 24
        t_max = (t0 + 6) % 24
        
        # Đề bài
        de_bai_chung = f"""Nhiệt độ ngoài trời ở một thành phố vào các thời điểm khác nhau trong ngày có thể được mô phỏng bởi công thức:
    $$h(t) = {a} + {b} \\sin\\left[\\frac{{\\pi}}{{12}}(t - {t0})\\right]$$
    với $h$ tính bằng °C và $t$ (giờ) là thời gian trong ngày. """
        
        hoi_giai_dapan = [
            (
                f"""Nhiệt độ thấp nhất trong ngày là bao nhiêu °C và vào lúc mấy giờ?""",
                f"""Nhiệt độ thấp nhất khi $\\sin\\left[\\frac{{\\pi}}{{12}}(t - {t0})\\right] = -1$.\\\\
    Khi đó: $$h_{{\\min}} = {a} - {b} = {h_min}\\ ^\\circ\\text{{C}}.$$
    Thời điểm đạt được khi: $$\\frac{{\\pi}}{{12}}(t - {t0}) = -\\frac{{\\pi}}{{2}} + 2k\\pi$$
    $$\\Rightarrow t = {t0} - 6 + 24k.$$
    Lấy $k=0$: $t = {t_min}\\ \\text{{giờ}}$.""",
                f"${h_min}\\ ^\\circ\\text{{C, lúc }}{t_min}\\ \\text{{giờ}}$",
                f"${h_max}\\ ^\\circ\\text{{C, lúc }}{t_max}\\ \\text{{giờ}}$",
                f"${h_min}\\ ^\\circ\\text{{C, lúc }}{t0}\\ \\text{{giờ}}$",
                f"${h_max}\\ ^\\circ\\text{{C, lúc }}{t0}\\ \\text{{giờ}}$",
            ),
            (
                f"""Nhiệt độ cao nhất trong ngày là bao nhiêu °C và vào lúc mấy giờ?""",
                f"""Nhiệt độ cao nhất khi $\\sin\\left[\\frac{{\\pi}}{{12}}(t - {t0})\\right] = 1$.\\\\
    Khi đó: $$h_{{\\max}} = {a} + {b} = {h_max}\\ ^\\circ\\text{{C}}.$$
    Thời điểm đạt được khi: $$\\frac{{\\pi}}{{12}}(t - {t0}) = \\frac{{\\pi}}{{2}} + 2k\\pi$$
    $$\\Rightarrow t = {t0} + 6 + 24k.$$
    Lấy $k=0$: $t = {t_max}\\ \\text{{giờ}}$.""",
                f"${h_max}\\ ^\\circ\\text{{C, lúc }}{t_max}\\ \\text{{giờ}}$",
                f"${h_min}\\ ^\\circ\\text{{C, lúc }}{t_min}\\ \\text{{giờ}}$",
                f"${h_min}\\ ^\\circ\\text{{C, lúc }}{t0}\\ \\text{{giờ}}$",
                f"${h_max}\\ ^\\circ\\text{{C, lúc }}{t0}\\ \\text{{giờ}}$",
            )
        ]
        
        # Chọn ngẫu nhiên câu hỏi
        de_TN = random.choice(hoi_giai_dapan)
        
        # Đáp án trắc nghiệm 4 lựa chọn
        da_dung = f"\\True {de_TN[2]}" 
        da_nhieu = [nhieu for nhieu in de_TN[3:] if nhieu != de_TN[2]]
        
        if len(set(da_nhieu)) < 3:
            print("Không đủ 3 đáp án nhiễu khác nhau. Cần viết thêm.")
        
        nhieu1, nhieu2, nhieu3 = random.sample(da_nhieu, 3)
        dap_an = [da_dung, nhieu1, nhieu2, nhieu3]
        random.shuffle(dap_an)
        
        phan_lua_chon = f"\n\\choice\n{{{dap_an[0]}}}\n{{{dap_an[1]}}}\n{{{dap_an[2]}}}\n{{{dap_an[3]}}}\n"
        
        # Xuất câu trắc nghiệm
        content = ('\\begin{minipage}{\\textwidth} \n' 
                '\\begin{ex}\n' + de_bai_chung + '\n' + de_TN[0] + phan_lua_chon +
                '\\loigiai{' + de_TN[1] + '}\n'
                '\\end{ex}\n\\end{minipage}\n\n').replace('\\frac', '\\dfrac')
        
        return content