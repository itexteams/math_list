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


def bt_dang2_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật và $SA$ vuông góc với mặt phẳng đáy. Gọi $H, K$ theo thứ tự là hình chiếu của $A$ trên các cạnh $SB,SD$.'''                 
                            %(
                                ))
            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tam giác $SBC$ là tam giác vuông'
            nb_da_1_s = 'Tam giác $SBC$ là tam giác đều'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.82,-0.64) rectangle (6.7,5.08);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (2.,4.);
                    \\draw [line width=1.pt] (2.,4.)-- (0.,0.);
                    \\draw [line width=1.pt] (2.,4.)-- (4.,0.);
                    \\draw [line width=1.pt] (2.,4.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (1.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (3.632,2.776);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.632,2.776)-- (1.,2.);
                    \\draw (1.7,4.6) node[anchor=north west] {$S$};
                    \\draw (1.78,1) node[anchor=north west] {$A$};
                    \\draw (-0.5,0.2) node[anchor=north west] {$B$};
                    \\draw (3.96,0) node[anchor=north west] {$C$};
                    \\draw (6.06,1.4) node[anchor=north west] {$D$};
                    \\draw (0.44,2.54) node[anchor=north west] {$H$};
                    \\draw (3.6,3.4) node[anchor=north west] {$K$};
                \\end{tikzpicture}
            \\end{center}
            Ta có: $\\heva{ &BC\\perp AB\\\\ &BC\\perp SA(\\text {do} SA\\perp (ABCD))}\\Rightarrow BC\\perp (SAB) $.\\\\
                Vì $\\heva{ &BC\\perp (SAB)\\\\ &SB\\subset(SAB)}\\Rightarrow BC\\perp SB $ hay $\\triangle SBC$ vuông tại $B$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tam giác $SCD$ là tam giác vuông' 
            th_da_1_s = 'Tam giác $SCD$ là tam giác đều'  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có: $\\heva{ &CD\\perp AD\\\\ &CD\\perp SA(\\text {do} SA\\perp (ABCD))}\\Rightarrow CD\\perp (SAD) $.\\\\
                Vì $\\heva{ &CD\\perp (SAD)\\\\ &SD\\subset(SAD)}\\Rightarrow CD\\perp SD $ hay $\\triangle SCD$ vuông tại $D$.'''       
                        %(
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $SC\\perp (AHK)$'
            vd_da_1_s = '$SC\\perp (BHK)$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có: $\\heva{ &AH\\perp SB\\\\ &AH\\perp BC(\\text {do}BC\\perp (SAB))}\\Rightarrow AH\\perp (SBC)\\Rightarrow AH\\perp SC $. (1)\\\\\\\\
                Tương tự: $\\heva{ &AK\\perp SD\\\\ &AK\\perp CD(\\text {do}CD\\perp (SAD))}\\Rightarrow AK\\perp (SCD)\\Rightarrow AK\\perp SC $. (2)\\\\\\\\
                Từ (1) và (2) suy ra $SC\\perp (AHK)$.'''  
                        %(
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $HK\\perp SC$'
            vdc_da_1_s = '$HK\\perp SB$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $SC\\perp (AHK)$, mà $HK\\subset(AHK)$ nên $HK\\perp SC$.'''
                        %(
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

