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


def bt_dang16_p2_b1_c2_hh11(self):
            # --- KHAI BÁO NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong không gian, cho hình lập phương $ABCD.A'B'C'D'$, gọi $M, N, E, F$ lần lượt là trung điểm của $BC, AB, AA', A'D'$.''')

            # --- NHẬN BIẾT ---
            nb_da_1_d = '\\True Cạnh $MN$ và $AA\'$ vuông góc với nhau'
            nb_da_1_s = 'Cạnh $MN$ và $AA\'$ song song với nhau'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $MN \\subset (ABCD)$. Vì $AA' \\perp (ABCD)$ nên $AA' \\perp MN$.''')

            # --- THÔNG HIỂU ---
            th_da_1_d = '\\True Góc giữa $MN$ và $CD\'$ bằng góc giữa $AC$ và $CD\'$'
            th_da_1_s = 'Góc giữa $MN$ và $CD\'$ bằng góc giữa $BD$ và $CD\'$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Vì $M, N$ là trung điểm của $BC, AB$ nên $MN$ là đường trung bình của $\\triangle ABC$, suy ra $MN \\parallel AC$. Do đó $(MN, CD') = (AC, CD')$.''')

            # --- VẬN DỤNG ---
            vd_da_1_d = '\\True Góc giữa $EF$ và $CC\'$ bằng góc giữa $AD\'$ và $CC\'$'
            vd_da_1_s = 'Góc giữa $EF$ và $CC\'$ bằng góc giữa $A\'D$ và $CC\'$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì $E, F$ là trung điểm của $AA', A'D'$ nên $EF$ là đường trung bình của $\\triangle AA'D'$, suy ra $EF \\parallel AD'$. Do đó $(EF, CC') = (AD', CC')$.''')

            # --- VẬN DỤNG CAO ---
            vdc_da_1_d = '\\True Góc giữa $EF$ và $CD\'$ bằng $60^\\circ$'
            vdc_da_1_s = 'Góc giữa $EF$ và $CD\'$ bằng $30^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $EF \\parallel AD'$. Suy ra $(EF, CD') = (AD', CD')$. \\\\
            Xét tam giác $ACD'$, ta có $AC = CD' = D'A = a\\sqrt{2}$ (với $a$ là cạnh hình lập phương). \\\\
            Do đó $\\triangle ACD'$ là tam giác đều, suy ra $\\widehat{AD'C} = 60^\\circ$. Vậy góc giữa $EF$ và $CD'$ bằng $60^\\circ$.''')

            # --- HÌNH VẼ TIKZ ---
            tikz_hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1.5, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-0.6);
                \\coordinate (C) at (3.5,-0.6);
                \\coordinate (D) at (2.3,0);
                \\coordinate (A1) at (0,2.5);
                \\coordinate (B1) at (1.2,1.9);
                \\coordinate (C1) at (3.5,1.9);
                \\coordinate (D1) at (2.3,2.5);
                \\coordinate (M) at ($(B)!0.5!(C)$);
                \\coordinate (N) at ($(A)!0.5!(B)$);
                \\coordinate (E) at ($(A)!0.5!(A1)$);
                \\coordinate (F) at ($(A1)!0.5!(D1)$);
                \\draw (B)--(C) (B)--(B1)--(C1) (C)--(C1) (D1)--(C1) (B1)--(A1) (A1)--(D1) (A)--(A1) (A)--(B);
                \\draw[dashed] (C)--(D1) (A)--(D) (D)--(D1) (D)--(C) (N)--(M) (E)--(F) (A)--(C);
                \\foreach \\p/\\pos in {A/left, B/below, C/right, D/right, A1/left, B1/left, C1/right, D1/right, M/below, N/left, E/left, F/above}
                \\node[\\pos] at (\\p) {$\\p$};
            \\end{tikzpicture}
            \\end{center}''')

            # --- LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # --- XUẤT NỘI DUNG THEO MẪU DANG15 ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n' +
                tikz_hinh_ve + '\n' +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

