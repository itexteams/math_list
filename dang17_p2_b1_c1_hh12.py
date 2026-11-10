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


def bt_dang17_p2_b1_c1_hh12(self):
    # Mã vẽ TikZ hình hộp ABCD.A'B'C'D' có tâm O chính xác 100% như ảnh[cite: 22]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2.4,0);
    \\coordinate (D) at (-1.1,-1.2);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (A') at (-1.1,2.4);
    \\coordinate (B') at ($(B)+(A')-(A)$);
    \\coordinate (D') at ($(D)+(A')-(A)$);
    \\coordinate (C') at ($(C)+(A')-(A)$);
    \\coordinate (O) at ($(A)!0.5!(C')$);
    \\draw[line width=1pt] (D')--(A')--(B')--(C')--cycle;
    \\draw[line width=1pt] (D')--(D)--(C)--(C') (B')--(B)--(C);
    \\draw[line width=1pt, dashed] (A')--(A)--(D) (A)--(B) (A')--(C) (A)--(C');
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (A') circle (1pt) node[left] {$A'$};
    \\fill (B') circle (1pt) node[right] {$B'$};
    \\fill (C') circle (1pt) node[right] {$C'$};
    \\fill (D') circle (1pt) node[left] {$D'$};
    \\fill (O) circle (1pt) node[right] {$O$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian cho hình hộp $ABCD.A'B'C'D'$ tâm $O$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Quy tắc hình hộp[cite: 22]
    nb_da_1_d = "\\True $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$"
    nb_da_1_s = "$\\vec{AC'} = \\vec{AB} + \\vec{AD} - \\vec{AA'}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Áp dụng quy tắc hình hộp cho ba cạnh xuất phát từ đỉnh $A$ là $AB, AD, AA'$ và đường chéo $AC'$, ta có: \\\\ $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$. \\\\ Thật vậy: $\\vec{AB} + \\vec{AD} = \\vec{AC}$ (theo quy tắc hình bình hành áp dụng cho đáy $ABCD$), \\\\ suy ra $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC} + \\vec{AA'} = \\vec{AC} + \\vec{CC'} = \\vec{AC'}$ (theo quy tắc ba điểm trong hình bình hành $ACC'A'$). \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Biểu thức tổng các vectơ liên tiếp[cite: 22]
    th_da_1_d = "\\True $\\vec{AB} + \\vec{BC'} + \\vec{C'D} + \\vec{D'A} \\neq \\vec{0}$"
    th_da_1_s = "$\\vec{AB} + \\vec{BC'} + \\vec{CD} + \\vec{D'A} = \\vec{0}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta biến đổi vế trái: \\\\ $(\\vec{AB} + \\vec{BC'}) + \\vec{CD} + \\vec{D'A} = \\vec{AC'} + \\vec{CD} + \\vec{D'A}$. \\\\ Vì trong hình hộp, $\\vec{CD} = \\vec{BA} = -\\vec{AB}$ và $\\vec{D'A} = -\\vec{AD'} = -(\\vec{AD} + \\vec{AA'})$, \\\\ đồng thời $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$. \\\\ Do đó: \\\\ $\\vec{AC'} + \\vec{CD} + \\vec{D'A} = (\\vec{AB} + \\vec{AD} + \\vec{AA'}) - \\vec{AB} - (\\vec{AD} + \\vec{AA'}) = \\vec{0} \\neq \\vec{0}$ là sai. \\\\ Cụ thể: $\\vec{AB} + \\vec{BC'} + \\vec{CD} + \\vec{D'A} = (\\vec{AB} + \\vec{CD}) + (\\vec{BC'} + \\vec{D'A}) = \\vec{0} + \\vec{0} = \\vec{0}$. \\\\ Do đó khẳng định $\\vec{AB} + \\vec{BC'} + \\vec{CD} + \\vec{D'A} = \\vec{0}$ là đúng."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: So sánh \vec{AB} + \vec{AA'} và \vec{AD} + \vec{DD'}[cite: 22]
    vd_da_1_d = "\\True $\\vec{AB} + \\vec{AA'} = \\vec{AB'}$ và $\\vec{AD} + \\vec{DD'} = \\vec{AD'}$ nên $\\vec{AB} + \\vec{AA'} \\neq \\vec{AD} + \\vec{DD'}$"
    vd_da_1_s = "$\\vec{AB} + \\vec{AA'} = \\vec{AD} + \\vec{DD'}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Áp dụng quy tắc hình bình hành: \\\\ $\\bullet$ Trong hình bình hành $ABB'A'$, ta có: $\\vec{AB} + \\vec{AA'} = \\vec{AB'}$. \\\\ $\\bullet$ Trong hình bình hành $ADD'A'$, ta có: $\\vec{DD'} = \\vec{AA'}$, do đó $\\vec{AD} + \\vec{DD'} = \\vec{AD} + \\vec{AA'} = \\vec{AD'}$. \\\\ Hai vectơ $\\vec{AB'}$ và $\\vec{AD'}$ lần lượt nằm trên hai mặt phẳng phân biệt $(ABB'A')$ và $(ADD'A')$, hai đường thẳng $AB'$ và $AD'$ cắt nhau tại đỉnh $A$ nên $\\vec{AB'} \\neq \\vec{AD'}$. \\\\ Suy ra $\\vec{AB} + \\vec{AA'} \\neq \\vec{AD} + \\vec{DD'}$. \\\\ Do đó khẳng định $\\vec{AB} + \\vec{AA'} = \\vec{AD} + \\vec{DD'}$ là sai."""
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Chèn điểm qua tâm O của hình hộp[cite: 22]
    vdc_da_1_d = (
        "\\True $\\vec{AB} + \\vec{BC} + \\vec{CC'} = \\vec{AD'} + \\vec{D'O} + \\vec{OC'}$"
    )
    vdc_da_1_s = (
        "$\\vec{AB} + \\vec{BC} + \\vec{CC'} = \\vec{AD'} + \\vec{D'O} - \\vec{OC'}$"
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta xét vế trái của đẳng thức: \\\\ $\\vec{AB} + \\vec{BC} + \\vec{CC'} = \\vec{AC} + \\vec{CC'} = \\vec{AC'}$. \\\\ Xét vế phải của đẳng thức, áp dụng quy tắc ba điểm cộng vectơ liên tiếp: \\\\ $\\vec{AD'} + \\vec{D'O} + \\vec{OC'} = (\\vec{AD'} + \\vec{D'O}) + \\vec{OC'} = \\vec{AO} + \\vec{OC'} = \\vec{AC'}$. \\\\ Vì cả hai vế đều bằng vectơ đường chéo $\\vec{AC'}$ của hình hộp nên đẳng thức luôn đúng với mọi điểm $O$ bất kì trong không gian (và đặc biệt khi $O$ là tâm hình hộp). \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in vdc_da_1 else "sai")
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    