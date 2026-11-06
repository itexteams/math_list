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


def bt_dang21_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng bài (random góc kết quả)
            lis_goc = [30, 45, 60]
            goc_dung = random.choice(lis_goc)

            # Thiết lập các thông số dựa trên góc được chọn
            # Đáy ABC luôn là tam giác đều cạnh a -> AH = a*sqrt(3)/2
            # Gọi h là chiều cao SH. Tan(goc) = SH / AH -> SH = AH * tan(goc)

            if goc_dung == 45:
                mota_SBC = "tam giác $SBC$ là tam giác đều"
                bieuthuc_SH = "\\frac{a\\sqrt{3}}{2}"
                ly_luan_SH = "Do tam giác $SBC$ đều cạnh $a$ nên chiều cao $SH = \\frac{a\\sqrt{3}}{2}$."
                dap_an_dung = "45^\\circ"
                ds_sai = ["30^\\circ", "60^\\circ", "90^\\circ"]
            elif goc_dung == 60:
                mota_SBC = "tam giác $SBC$ cân tại $S$ và có diện tích bằng $\\frac{3a^2}{4}$"
                bieuthuc_SH = "\\frac{3a}{2}"
                ly_luan_SH = "Diện tích tam giác $SBC$ là $S = \\frac{1}{2}SH \\cdot BC \\Rightarrow \\frac{3a^2}{4} = \\frac{1}{2}SH \\cdot a \\Rightarrow SH = \\frac{3a}{2}$."
                dap_an_dung = "60^\\circ"
                ds_sai = ["45^\\circ", "30^\\circ", "75^\\circ"]
            else: # 30 do
                mota_SBC = "tam giác $SBC$ cân tại $S$ và có chiều cao $SH = \\frac{a}{2}$"
                bieuthuc_SH = "\\frac{a}{2}"
                ly_luan_SH = "Theo giả thiết, chiều cao của tam giác $SBC$ là $SH = \\frac{a}{2}$."
                dap_an_dung = "30^\\circ"
                ds_sai = ["45^\\circ", "60^\\circ", "15^\\circ"]

            # Tạo danh sách đáp án
            da_d = "\\True $" + dap_an_dung + "$"
            list_da = [da_d]
            for s in ds_sai:
                list_da.append("$" + s + "$")
            random.shuffle(list_da)

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. "
                             "Hình chiếu vuông góc của $S$ lên mặt phẳng $\\left( ABC \\right)$ trùng với trung điểm $H$ của cạnh $BC$. "
                             "Biết " + mota_SBC + ". Góc giữa đường thẳng $SA$ và mặt phẳng $\\left( ABC \\right)$ bằng bao nhiêu?")

            # Vẽ hình bằng TikZ
            tikz_code = ("\\begin{center}\n"
                         "\\begin{tikzpicture}[scale=1, line width=1pt, join=round, cap=round]\n"
                         "\\coordinate (H) at (0,-0.5);\n"
                         "\\coordinate (B) at (-1.5,-0.5);\n"
                         "\\coordinate (C) at (1.5,-0.5);\n"
                         "\\coordinate (A) at (-1,-2);\n"
                         "\\coordinate (S) at (0,3);\n"
                         "\\draw[dashed] (B)--(C)  (S)--(H) (A)--(H);\n"
                         "\\draw (S)--(A)--(B)--(S)--(C) (A)--(C);\n"
                         "\\filldraw (S)  node[above] {$S$}\n"
                         "          (A)  node[left] {$A$}\n"
                         "          (B)  node[below left] {$B$}\n"
                         "          (C) node[right] {$C$}\n"
                         "          (H)  node[above right] {$H$};\n"
                         "\\end{tikzpicture}\n"
                         "\\end{center}")

            # Lời giải chi tiết
            loigiai = ("Vì $SH \\perp \\left( ABC \\right)$ nên $H$ là hình chiếu vuông góc của $S$ lên mặt phẳng $\\left( ABC \\right)$.\\\\ \n"
                       "Suy ra $AH$ là hình chiếu vuông góc của $SA$ lên mặt phẳng $\\left( ABC \\right)$.\\\\ \n"
                       "Do đó, góc giữa đường thẳng $SA$ và mặt phẳng $\\left( ABC \\right)$ là góc $\\widehat{SAH}$.\\\\ \n"
                       "Vì tam giác $ABC$ đều cạnh $a$ nên $AH = \\frac{a\\sqrt{3}}{2}$.\\\\ \n"
                       + ly_luan_SH + "\\\\ \n"
                       "Xét tam giác $SAH$ vuông tại $H$, ta có: \n"
                       "$\\tan \\widehat{SAH} = \\frac{SH}{AH} = \\frac{" + bieuthuc_SH + "}{\\frac{a\\sqrt{3}}{2}}$.\\\\ \n"
                       "Từ đó suy ra $\\widehat{SAH} = " + dap_an_dung + "$.")
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(dap_an_dung).replace('^\\circ', '')

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                       '\\loigiai{' + tikz_code+ loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

