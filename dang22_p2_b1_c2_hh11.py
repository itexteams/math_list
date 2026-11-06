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


def bt_dang22_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            val_a = random.randint(2, 6) # Chọn a là một số nguyên ngẫu nhiên từ 2 đến 6
            a_sym = symbols('a')

            # Các thông số bài toán theo a
            # AB = 2a, AD = a, DC = a, SA = 2a*sqrt(3)/3
            SA_val = latex(Rational(2 * val_a, 3)) + r'\sqrt{3}'
            AB_val = str(2 * val_a)
            AD_val = str(val_a)
            DC_val = str(val_a)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình thang vuông tại $A$ và $D$. Gọi $E$ là trung điểm của $AB$. Biết $AB = %s, AD = DC = %s$, đồng thời $SA \perp AB, SA \perp AD$ và $SA = %s$. 
            \begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,0);
                \coordinate (B) at (5,0);
                \coordinate (D) at (1.5,1.5);
                \coordinate (C) at (3.5,1.5);
                \coordinate (S) at (0,4);
                \coordinate (E) at (2.5,0);
                \draw[dashed] (S)--(D) (D)--(C) (A)--(D) (D)--(E) (E)--(C);
                \draw (S)--(A)--(B)--(S)--(C)--(B) ;
                \draw[fill=black] (A)  node[left] {$A$};
                \draw[fill=black] (B)  node[right] {$B$};
                \draw[fill=black] (C)  node[above right] {$C$};
                \draw[fill=black] (D)  node[above left] {$D$};
                \draw[fill=black] (E)  node[below] {$E$};
                \draw[fill=black] (S)  node[above] {$S$};
            \end{tikzpicture}
            \end{center}
            Khi đó:''' % (AB_val, AD_val, SA_val))

            ########################################################################
            # Nhận biết - Câu (a): Góc giữa SB và DC
            nb_da_1_d = r'\True $(SB, DC) = \widehat{SBA}$'
            nb_da_1_s = r'$(SB, DC) = \widehat{SBC}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Vì $ABCD$ là hình thang vuông tại $A, D$ và $DC=a, AB=2a$ nên $DC \parallel AB$.\\
            Do đó $(SB, DC) = (SB, AB) = \widehat{SBA}$.''')

            ########################################################################
            # Thông hiểu - Câu (b): Tính tan SBA
            # tan(SBA) = SA/AB = (2a*sqrt(3)/3) / 2a = sqrt(3)/3
            th_da_1_d = r'\True $\tan \widehat{SBA} = \frac{\sqrt{3}}{3}$'
            th_da_1_s = r'$\tan \widehat{SBA} = \frac{\sqrt{3}}{2}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Vì $SA \perp AB$ và $SA \perp AD$ nên $SA \perp (ABCD) \Rightarrow SA \perp AB$.\\
            Trong tam giác vuông $SAB$, ta có $\tan \widehat{SBA} = \frac{SA}{AB} = \frac{\frac{2a\sqrt{3}}{3}}{2a} = \frac{\sqrt{3}}{3}$.''')

            ########################################################################
            # Vận dụng - Câu (c): Quan hệ DE và BC
            vd_da_1_d = r'\True $DE \parallel BC$'
            vd_da_1_s = r'$DE \perp BC$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Gọi $E$ là trung điểm của $AB$ thì $AE = EB = a$.\\
            Vì $DC \parallel EB$ và $DC = EB = a$ nên tứ giác $EBCD$ là hình bình hành.\\
            Suy ra $DE \parallel BC$.''')

            ########################################################################
            # Vận dụng cao - Câu (d): Góc giữa SD và BC
            # Cos(SD, BC) = Cos(SD, ED) = sqrt(3/14). Góc xấp xỉ 62.45 độ.
            vdc_da_1_d = r'\True $(SD, BC) \approx 62,45^\circ$'
            vdc_da_1_s = r'$(SD, BC) \approx 52,42^\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Ta có $DE \parallel BC$ nên $(SD, BC) = (SD, DE) = \widehat{SDE}$.\\
            Tính các cạnh của tam giác $SDE$:\\
            $SD = \sqrt{SA^2 + AD^2} = \sqrt{\frac{4a^2}{3} + a^2} = a\sqrt{\frac{7}{3}}$.\\
            $SE = \sqrt{SA^2 + AE^2} = \sqrt{\frac{4a^2}{3} + a^2} = a\sqrt{\frac{7}{3}}$.\\
            $DE = \sqrt{AD^2 + AE^2} = \sqrt{a^2 + a^2} = a\sqrt{2}$.\\
            Áp dụng định lý hàm số cos trong tam giác $SDE$:\\
            $\cos \widehat{SDE} = \frac{SD^2 + DE^2 - SE^2}{2 \cdot SD \cdot DE} = \frac{\frac{7a^2}{3} + 2a^2 - \frac{7a^2}{3}}{2 \cdot a\sqrt{\frac{7}{3}} \cdot a\sqrt{2}} = \frac{2a^2}{2a^2\sqrt{\frac{14}{3}}} = \sqrt{\frac{3}{14}}$.\\
            Suy ra $\widehat{SDE} \approx 62,45^\circ$.''')

            ########################################################################
            # Kiểm tra số lượng đáp án đúng (từ 1 đến 3)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
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

