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


def bt_dang1_p2_b4_c1_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = 'Cho hình lăng trụ $ABCD.A\'B\'C\'D\'$ có đáy là hình bình hành. $M, N, P$ lần lượt là trung điểm của các cạnh $AD, BC, CC\'$.' 

            hinhve = (   

                    '\\begin{center}  \n'
                    '\\scalebox{0.7}{' 
                        '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]  \n'
                            '\\clip(-0.9198164187841548,-0.8428093140230718) rectangle (7.335596121325123,6.0137694345676955); \n'
                            '\\draw (0.,0.)-- (4.,0.); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (6.,2.); \n'
                            '\\draw (6.,2.)-- (4.,0.); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,5.); \n'
                            '\\draw (0.,0.)-- (0.,3.); \n'
                            '\\draw (0.,3.)-- (2.,5.); \n'
                            '\\draw (4.,0.)-- (4.,3.); \n'
                            '\\draw (6.,2.)-- (6.,5.); \n'
                            '\\draw (6.,5.)-- (2.,5.); \n'
                            '\\draw (0.,3.)-- (4.,3.); \n'
                            '\\draw (4.,3.)-- (6.,5.); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.9771172534905859,0.9771172534905859)-- (4.982969123233022,0.9829691232330218); \n'
                            '\\draw (4.,1.5360782865753202)-- (4.982969123233022,0.9829691232330218); \n'
                            '\\draw (4.,1.5360782865753202)-- (0.,1.5055950630908013); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,1.5055950630908013)-- (0.9771172534905859,0.9771172534905859); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,3.)-- (2.,2.); \n'
                            '\\draw (4.,3.)-- (6.,2.); \n'
                            '\\draw (1.9695779702540928,2.5) node[anchor=north west] {$A$}; \n'
                            '\\draw (6.051420837308124,2.4364240005203386) node[anchor=north west] {$B$}; \n'
                            '\\draw (3.8729091947792873,0) node[anchor=north west] {$C$}; \n'
                            '\\draw (-0.43825068727778016,0) node[anchor=north west] {$D$}; \n'
                            '\\draw (1.6943975522504502,5.7385890165640525) node[anchor=north west] {$A\'$}; \n'
                            '\\draw (5.730377016303875,5.715657315063749) node[anchor=north west] {$B\'$}; \n'
                            '\\draw (3.6779897320267074,3.7091334337871866) node[anchor=north west] {$C\'$}; \n'
                            '\\draw (-0.49557994102853903,3.560077374035213) node[anchor=north west] {$D\'$}; \n'
                            '\\draw (4.904835762292947,1.2669072240048564) node[anchor=north west] {$N$}; \n'
                            '\\draw (0.8344587459890669,1) node[anchor=north west] {$M$}; \n'
                            '\\draw (4.033431105281412,2) node[anchor=north west] {$P$}; \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (4.,1.5360782865753198)-- (0.9771172534905859,0.9771172534905859); \n'
                        '\\end{tikzpicture} } \n'
                    '\\end{center}    \n'  

                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $A\'B\' // (MNP)$'
            nb_da_1_s = '$A\'D\' // (MNP)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $C\'D\' // (MNP)$'
            nb_da_2_s = '$C\'B\' // (MNP)$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vì $A\'B\' // AB$ và $AB // MN$ suy ra $A\'B\' // MN$, do đó $A\'B\' // (MNP)$.'
                        )
            loigiai_nb_2 = ('Vì $C\'D\' // AB$ và $AB // MN$ suy ra $C\'D\' // MN$, do đó $C\'D\' // (MNP)$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $(MNP) // (BC\'D\')$'
            th_da_1_s = '$(MNP) // (BC\'A\')$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $(MNP) // (AC\'D\')$'
            th_da_2_s = '$(MNP) // (AC\'B\')$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $C\'D\' // MN \\Rightarrow C\'D\' // (MNP)$. \\\\ \n'
                            '\\hspace*{1cm} $BC\' // NP \\Rightarrow BC\' // (MNP)$. \\\\ \n'
                            'Mà $C\'D\'$ và $BC\' $ cùng nằm trên mặt phẳng $(BC\'D\')$. Vậy $(MNP) // (BC\'D\')$.'
                        )
            loigiai_th_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $C\'D\' // MN \\Rightarrow C\'D\' // (MNP)$. \\\\ \n'
                            '\\hspace*{1cm} $AD\' // NP \\Rightarrow AD\' // (MNP)$. \\\\ \n'
                            'Mà $C\'D\'$ và $AD\'$ cùng nằm trên mặt phẳng $(AC\'D\')$. Vậy $(MNP) // (AC\'D\')$.'
                            )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $(MNP) // (ABC\'D\')$'
            vd_da_1_s = '$(MNP) // (ABA\'B\')$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $C\'D\' // MN \\Rightarrow C\'D\' // (MNP)$. \\\\ \n'
                            '\\hspace*{1cm} $AD\' // NP \\Rightarrow AD\' // (MNP)$. \\\\ \n'
                            'Mà $C\'D\'$ và $AD\'$ cùng nằm trên mặt phẳng $(ABC\'D\')$. Vậy $(MNP) // (ABC\'D\')$.'
                            )
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
            vdc_da_1_d = '\\True $DD\'$ cắt $(MNP)$'
            vdc_da_1_s = '$DD\'$ song song $(MNP)$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True $AA\'$ cắt $(MNP)$'
            vdc_da_2_s = '$AA\'$ song song $(MNP)$'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $(MNP) // (BC\'D\')$ và $DD\' \\cap (BC\'D\')$. \\\\ \n'
                            'Suy ra $DD\'$ cắt $(MNP)$.'

                        )

            loigiai_vdc_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $(MNP) // (ABC\'D\')$ và $AA\' \\cap (ABC\'D\')$. \\\\ \n'
                            'Suy ra $AA\'$ cắt $(MNP)$.'

                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

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
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

