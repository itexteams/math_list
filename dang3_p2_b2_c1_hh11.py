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


def bt_dang3_p2_b2_c1_hh11(self):
    # Hình vẽ TikZ
    hinhve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
        '\\clip(-1.852641173982923,-0.5433119900481679) rectangle (6.106345612600232,4.922684771943773);\n'
        '\\draw (0.,0.)-- (4.,0.);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (1.,1.5);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (1.,1.5)-- (5.,1.5);\n'
        '\\draw (4.,0.)-- (5.,1.5);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (1.5,4.)-- (1.,1.5);\n'
        '\\draw (1.5,4.)-- (0.,0.);\n'
        '\\draw (1.5,4.)-- (4.,0.);\n'
        '\\draw (1.5,4.)-- (5.,1.5);\n'
        '\\draw (0.5,4.)-- (5.,4.);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (1.25,2.75)-- (3.25,2.75);\n'
        '\\draw [dash pattern=on 1pt off 1pt] (1.25,2.75)-- (0.5,0.75);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (0.5,0.75)-- (3.25,2.75);\n'
        '\\draw [dash pattern=on 2pt off 2pt] (0.5,0.75)-- (4.5,0.75);\n'
        '\\draw (0.5,2.5)-- (1.8811774308995346,4.571766146349302);\n'
        '\\draw (1.2442408441428183,4.643965390312456) node[anchor=north west] {$S$};\n'
        '\\draw (1.1048811533271599,2.1045221354493444) node[anchor=north west] {$A$};\n'
        '\\draw (-0.2577469346481663,0) node[anchor=north west] {$B$};\n'
        '\\draw (3.8301373292778123,0.15) node[anchor=north west] {$C$};\n'
        '\\draw (5,1.841287163908656) node[anchor=north west] {$D$};\n'
        '\\draw (3.2,3.281337302337128) node[anchor=north west] {$P$};\n'
        '\\draw (1.3216628945959619,3.327790532609014) node[anchor=north west] {$M$};\n'
        '\\draw (0.45,0.8) node[anchor=north west] {$N$};\n'
        '\\draw (4.588873423718619,1.0515822492865912) node[anchor=north west] {$Q$};\n'
        '\\draw (2.2816963202149414,1.3612704510991656) node[anchor=north west] {$d\'$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
    )

    # Nội dung câu hỏi
    noidungcauhoi = 'Cho hình chóp ${S.ABCD}$ có đáy ${ABCD}$ là hình bình hành. Gọi ${M, N, P}$ lần lượt là trung điểm của các cạnh ${SA, AB, SD}$.'

    # 1. Giao tuyến (SBC) và (SAD)
    da_1_d = '\\True ${(SBC)\\cap (SAD)=d}$ với $d$ là đường thẳng đi qua $S$ và song song với $AD$ và $BC$'
    da_1_s = '${(SBC)\\cap (SAD)=d}$ với $d$ là đường thẳng đi qua $S$ và song song với $AB$ và $CD$'
    lg_1 = 'Hai mặt phẳng ${(SBC)}$ và ${(SAD)}$ có điểm chung ${S}$ và lần lượt chứa hai đường thẳng song song là $AD$ và $BC$ nên giao tuyến của chúng là đường thẳng ${d}$ đi qua ${S}$ và song song với $AD$ và $BC$.'

    # 2. Giao tuyến (MNP) và (ABCD) - Sửa lỗi đồng bộ kí hiệu d'
    da_2_d = '\\True ${(MNP)\\cap (ABCD)=d\'}$ với $d\'$ là đường thẳng đi qua $N$ và song song với $AD$ và $MP$'
    da_2_s = '${(MNP)\\cap (ABCD)=d\'}$ với $d\'$ là đường thẳng đi qua $N$ và song song với $AB$ và $CD$'
    lg_2 = 'Do $MP$ là đường trung bình của tam giác ${SAD}$ nên ${MP \\parallel AD}$. Hai mặt phẳng ${(MNP)}$ và ${(ABCD)}$ có điểm chung ${N}$ và lần lượt chứa hai đường thẳng song song là $MP$ và $AD$ nên giao tuyến của chúng là đường thẳng $d\'$ đi qua ${N}$ và song song với $AD$ và $MP$.'

    # 3. Giao tuyến (MNP) và (SAD)
    da_3_d = '\\True ${(MNP)\\cap (SAD)=MP}$'
    da_3_s = '${(MNP)\\cap (SAD)=MN}$'
    lg_3 = 'Ta có $M\\in SA \\subset (SAD) \\Rightarrow M\\in (SAD)$ và $P\\in SD \\subset (SAD) \\Rightarrow P\\in (SAD)$. Mà $M,P \\in (MNP)$ nên ${(MNP)\\cap (SAD)=MP}$.'

    # 4. Giao tuyến (MNP) và (SAB)
    da_4_d = '\\True ${(MNP)\\cap (SAB)=MN}$'
    da_4_s = '${(MNP)\\cap (SAB)=PN}$'
    lg_4 = 'Ta có $M\\in SA \\subset (SAB) \\Rightarrow M\\in (SAB)$ và $N\\in AB \\subset (SAB) \\Rightarrow N\\in (SAB)$. Mà $M,N \\in (MNP)$ nên ${(MNP)\\cap (SAB)=MN}$.'

    # 5. Giao tuyến (MNP) và (SCD) - Sửa câu trùng lặp với câu 3
    da_5_d = '\\True ${(MNP)\\cap (SCD)=PQ}$ với $Q$ là trung điểm của $CD$'
    da_5_s = '${(MNP)\\cap (SCD)=SC}$'
    lg_5 = 'Gọi $Q$ là trung điểm của $CD$. Khi đó $NQ \\parallel AD \\parallel MP$ nên $NQ \\subset (MNP)$, suy ra $Q \\in (MNP)$. Lại có $Q \\in CD \\subset (SCD)$ và $P \\in SD \\subset (SCD)$. Vậy ${(MNP)\\cap (SCD)=PQ}$.'

    # 6. Giao tuyến (SAB) và (SCD)
    da_6_d = '\\True ${(SAB)\\cap (SCD)=\\Delta}$ với $\\Delta$ là đường thẳng đi qua $S$ và song song với $AB$ và $CD$'
    da_6_s = '${(SAB)\\cap (SCD)=\\Delta}$ với $\\Delta$ là đường thẳng đi qua $S$ và song song với $AD$ và $BC$'
    lg_6 = 'Hai mặt phẳng ${(SAB)}$ và ${(SCD)}$ có điểm chung ${S}$ và lần lượt chứa hai đường thẳng song song là $AB$ và $CD$ nên giao tuyến của chúng là đường thẳng ${\\Delta}$ đi qua ${S}$ và song song với $AB$ và $CD$.'

    # 7. Giao tuyến (SAC) và (SBD)
    da_7_d = '\\True ${(SAC)\\cap (SBD)=SO}$ với $O$ là giao điểm của $AC$ và $BD$'
    da_7_s = '${(SAC)\\cap (SBD)=SO}$ với $O$ là giao điểm của $MN$ và $AC$'
    lg_7 = 'Hai mặt phẳng $(SAC)$ và $(SBD)$ có điểm chung $S$. Gọi $O = AC \\cap BD$, ta có $O \\in AC \\subset (SAC)$ và $O \\in BD \\subset (SBD)$, suy ra $O \\in (SAC) \\cap (SBD)$. Vậy ${(SAC)\\cap (SBD)=SO}$.'

    # Gom các cặp (đáp án đúng, đáp án sai, lời giải)
    cau_hoi_pool = [
        (da_1_d, da_1_s, lg_1),
        (da_2_d, da_2_s, lg_2),
        (da_3_d, da_3_s, lg_3),
        (da_4_d, da_4_s, lg_4),
        (da_5_d, da_5_s, lg_5),
        (da_6_d, da_6_s, lg_6),
        (da_7_d, da_7_s, lg_7)
    ]

    # Chọn ngẫu nhiên 4 mệnh đề không trùng nhau và đảm bảo có từ 1 đến 3 ý Đúng
    while True:
        selected_items = random.sample(cau_hoi_pool, 4)
        chosen_answers = []
        chosen_solutions = []
        for item in selected_items:
            is_correct = random.choice([True, False])
            chosen_answers.append(item[0] if is_correct else item[1])
            chosen_solutions.append(item[2])

        true_count = sum('\\True' in ans for ans in chosen_answers)
        if 1 <= true_count <= 3:
            break

    # Xuất câu hỏi trắc nghiệm Đúng/Sai
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choiceTFn\n'
        '{' + str(chosen_answers[0]) + '}\n'
        '{' + str(chosen_answers[1]) + '}\n'
        '{' + str(chosen_answers[2]) + '}\n'
        '{' + str(chosen_answers[3]) + '}\n'
        '\\loigiai{' + str(hinhve) + '\n'
        '\\begin{enumEX}[a)]{1}\n'
        '\\item ' + str(chosen_solutions[0]) + '\n'
        '\\item ' + str(chosen_solutions[1]) + '\n'
        '\\item ' + str(chosen_solutions[2]) + '\n'
        '\\item ' + str(chosen_solutions[3]) + '\n'
        '\\end{enumEX}}\n'
        '\\end{ex}\n\\end{minipage}\n\n' )
    return content

