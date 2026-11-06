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


def bt_dang4_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $O$ và $SA=SC, SB=SD$.''')

            # Hình vẽ TikZ theo yêu cầu: nét vẽ 1pt, giống 100% hình trong ảnh
            hinh_ve = r'''\begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
            \coordinate (O) at (0,0);
            \coordinate (A) at (-1.2,1);
            \coordinate (B) at (-2.5,-1);
            \coordinate (C) at (1.2,-1);
            \coordinate (D) at (2.5,1);
            \coordinate (S) at (-0.5,3);
            \draw[line width=1pt, dashed] (A)--(D) (A)--(B) (A)--(C) (B)--(D) (S)--(A) (S)--(O);
            \draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
            \node[left] at (A) {$A$};
            \node[left] at (B) {$B$};
            \node[right] at (C) {$C$};
            \node[right] at (D) {$D$};
            \node[above] at (S) {$S$};
            \node[below] at (O) {$O$};
            \draw[line width=1pt] (-0.2,0.1) -- (-0.2,0.3) -- (0,0.2);
            \end{tikzpicture}'''

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = r'\True $SO \perp AC$'
            nb_da_1_s = r'$SO$ không vuông góc với $AC$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Tam giác $SAC$ cân tại $S$ (do $SA=SC$), mà $O$ là trung điểm $AC$ nên $SO \perp AC$. (1)''')

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = r'\True $SO \perp \left(ABCD\right)$ '
            th_da_1_s = r'$SO \perp \left(SBD\right)$ '
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Tam giác $SBD$ cân tại $S$ (do $SB=SD$), mà $O$ là trung điểm $BD$ nên $SO \perp BD$. (2) \\ Từ (1) và (2) suy ra $SO \perp \left(ABCD\right)$.''')

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = r'\True $AC \perp \left(SBD\right)$ '
            vd_da_1_s = r'$AC \parallel \left(SBD\right)$ '
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Ta có $\begin{cases} AC \perp BD \\ AC \perp SO \text{ do } SO \perp \left(ABCD\right) \end{cases} \Rightarrow AC \perp \left(SBD\right)$.''')

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = r'$\left(AC, SB\right) = 90^\circ$' # Phương án sai (theo đề bài là 60 nhưng thực tế 90)
            vdc_da_1_s = r'\True $\left(AC, SB\right) = 60^\circ$' # Đảo lại để khớp logic chọn True/Sai ngẫu nhiên

            # Để đúng cấu trúc ảnh: d là Sai.
            # Ta thiết lập: d là Sai nếu chọn 60 độ, Đúng nếu chọn 90 độ.
            vdc_da_1_true = r'\True $\left(AC, SB\right) = 90^\circ$'
            vdc_da_1_false = r'$\left(AC, SB\right) = 60^\circ$'
            list_vdc_da_1 = [vdc_da_1_true, vdc_da_1_false]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Mà $SB \subset \left(SBD\right)$ nên $AC \perp SB \Rightarrow \left(AC, SB\right) = 90^\circ$.''')

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                choice_nb = random.choice(list_nb_da_1)
                choice_th = random.choice(list_th_da_1)
                choice_vd = random.choice(list_vd_da_1)
                choice_vdc = random.choice(list_vdc_da_1)

                current_answers = [choice_nb, choice_th, choice_vd, choice_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [choice_nb, choice_th, choice_vd, choice_vdc]
            # Lời giải tương ứng (trong bài này lời giải là cố định cho tính chất hình học)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\begin{center}\n' + hinh_ve + '\n\\end{center}\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

