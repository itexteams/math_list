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


def bt_dang58_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các biến và danh sách dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Random tên cạnh của hình vuông để tạo sự khác biệt nhẹ
                ten_canh = random.choice(['a', 'b', 'x', 'm'])

                # Góc đúng của bài toán này luôn là 60 độ do tính chất tam giác đều AMN
                kq_dung = '60^\\circ'

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                cac_phuong_an_sai = ['30^\\circ', '45^\\circ', '90^\\circ', '120^\\circ', '150^\\circ']
                random.shuffle(cac_phuong_an_sai)

                # Chọn ra 3 đáp án sai từ danh sách
                das1 = '$' + cac_phuong_an_sai[0] + '$'
                das2 = '$' + cac_phuong_an_sai[1] + '$'
                das3 = '$' + cac_phuong_an_sai[2] + '$'

                da_dung = '$' + kq_dung + '$'

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $%s$, cạnh bên $SA$ vuông góc với đáy, $SA = %s$. Gọi $M$ là trung điểm $SB$. Góc giữa $AM$ và $BD$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (ten_canh, ten_canh))

                # Mã TikZ cho hình vẽ
                tikz_hinh = '''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (D) at (-1.2,-1.5);
                \\coordinate (B) at (3.5,0);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (S) at (0,3);
                \\coordinate (M) at ($(S)!0.5!(B)$);
                \\coordinate (N) at ($(S)!0.5!(D)$);
                \\draw (S)--(D)--(C)--(B)--(S)--(C);
                \\draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(M) (A)--(N) (M)--(N);
                \\foreach \\p/\\pos in {S/above, A/left, B/right, C/right, D/left, M/right, N/left}
                \\fill (\\p) node[\\pos] {$\\p$};
            \\end{tikzpicture}
            \\end{center}'''

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt và chi tiết)
                loigiai = (tikz_hinh + '''Gọi $N$ là trung điểm của $SD$. \\\\
                           Vì $M, N$ lần lượt là trung điểm của $SB$ và $SD$ nên $MN$ là đường trung bình của tam giác $SBD$. \\\\
                           Suy ra $MN \\parallel BD$, do đó góc giữa $AM$ và $BD$ bằng góc giữa $AM$ và $MN$. \\\\
                           Ta có $(BD; AM) = (MN; AM) = \\widehat{AMN}$ (hoặc bù với góc này). \\\\
                           Xét các tam giác vuông $SAB$ và $SAD$: \\\\
                           $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{%s^2 + %s^2} = %s\\sqrt{2}$. \\\\
                           $SD = \\sqrt{SA^2 + AD^2} = \\sqrt{%s^2 + %s^2} = %s\\sqrt{2}$. \\\\
                           Vì $M, N$ là trung điểm các cạnh huyền nên: \\\\
                           $AM = \\frac{1}{2}SB = \\frac{%s\\sqrt{2}}{2}$. \\\\
                           $AN = \\frac{1}{2}SD = \\frac{%s\\sqrt{2}}{2}$. \\\\
                           Lại có $MN = \\frac{1}{2}BD = \\frac{1}{2}\\sqrt{AB^2 + AD^2} = \\frac{%s\\sqrt{2}}{2}$. \\\\
                           Suy ra $AN = AM = MN = \\frac{%s\\sqrt{2}}{2}$. \\\\
                           Do đó tam giác $AMN$ là tam giác đều, nên $\\widehat{AMN} = 60^\\circ$. \\\\
                           Vậy góc giữa $AM$ và $BD$ bằng $60^\\circ$.''' 
                           % (ten_canh, ten_canh, ten_canh, ten_canh, ten_canh, ten_canh, 
                              ten_canh, ten_canh, ten_canh, ten_canh))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(60))
                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Đảm bảo cấu trúc content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

